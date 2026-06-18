"""Connect to an existing orchestration deployment or auto-detect / deploy one."""

from __future__ import annotations

import os
import time
from typing import Callable

from ai_api_client_sdk.models.status import Status
from ai_core_sdk.ai_core_v2_client import AICoreV2Client
from gen_ai_hub.proxy import get_proxy_client


def spinner(
    check_callback: Callable,
    timeout: int = 300,
    check_every_n_seconds: int = 10,
):
    start = time.time()
    last_check = start
    while time.time() - start < timeout:
        now = time.time()
        if now - last_check > check_every_n_seconds:
            return_value = check_callback()
            if return_value:
                return return_value
            last_check = now
        time.sleep(1)
    return None


def retrieve_or_deploy_orchestration(
    ai_core_client: AICoreV2Client,
    scenario_id: str = "orchestration",
    executable_id: str = "orchestration",
    config_suffix: str = "tutorial",
    start_timeout: int = 300,
):
    """Find a RUNNING orchestration deployment or create one."""
    if not config_suffix:
        raise ValueError("Empty `config_suffix` not allowed")

    deployments = ai_core_client.deployment.query(
        scenario_id=scenario_id,
        executable_ids=[executable_id],
        status=Status.RUNNING,
    )
    if deployments.count > 0:
        return sorted(deployments.resources, key=lambda x: x.start_time)[0]

    config_name = f"{config_suffix}-orchestration"
    configs = ai_core_client.configuration.query(
        scenario_id=scenario_id,
        executable_ids=[executable_id],
        search=config_name,
    )
    if configs.count > 0:
        config = sorted(configs.resources, key=lambda x: x.creation_time)[0]
    else:
        config = ai_core_client.configuration.create(
            scenario_id=scenario_id,
            executable_id=executable_id,
            name=config_name,
        )

    deployment = ai_core_client.deployment.create(configuration_id=config.id)

    def check_ready():
        updated = ai_core_client.deployment.get(deployment.id)
        return updated if updated.status == Status.RUNNING else None

    ready = spinner(check_ready, timeout=start_timeout)
    if ready is None:
        raise TimeoutError(
            f"Orchestration deployment {deployment.id} did not reach RUNNING within {start_timeout}s."
        )
    return ready


def get_orchestration_deployment_url(ai_core_client: AICoreV2Client | None = None) -> str:
    """
    Resolve orchestration deployment URL.

    Priority:
    1. ORCH_DEPLOYMENT_URL environment variable (from config.json)
    2. First RUNNING orchestration deployment in the resource group
    3. Auto-deploy orchestration (fallback)
    """
    explicit_url = os.environ.get("ORCH_DEPLOYMENT_URL")
    if explicit_url:
        print("Using ORCH_DEPLOYMENT_URL from configuration.")
        return explicit_url

    client = ai_core_client
    if client is None:
        proxy = get_proxy_client()
        client = proxy.ai_core_client

    deployments = client.deployment.query(
        scenario_id="orchestration",
        executable_ids=["orchestration"],
        status=Status.RUNNING,
    )
    if deployments.count > 0:
        deployment = sorted(deployments.resources, key=lambda x: x.start_time)[0]
        print(f"Auto-detected orchestration deployment: {deployment.id}")
        return deployment.deployment_url

    print("No RUNNING orchestration deployment found. Creating one (see docs/02-orchestration.md).")
    deployment = retrieve_or_deploy_orchestration(client)
    return deployment.deployment_url
