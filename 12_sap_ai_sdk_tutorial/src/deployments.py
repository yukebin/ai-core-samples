"""List AI Core deployments via the Generative AI Hub proxy."""

from __future__ import annotations

import os
from typing import Any

from ai_api_client_sdk.models.status import Status
from gen_ai_hub.proxy import get_proxy_client


def get_proxy():
    """Return a configured Generative AI Hub proxy client."""
    return get_proxy_client()


def list_running_deployments(
    proxy: Any | None = None,
    *,
    print_summary: bool = True,
) -> tuple[Any, Any]:
    """
    Query RUNNING deployments in the configured resource group.

    Returns (deployments, proxy) so callers can reuse the same proxy client.
    """
    client = proxy or get_proxy_client()
    deployments = client.ai_core_client.deployment.query(status=Status.RUNNING)

    if print_summary:
        print(
            f"RUNNING deployments in resource group "
            f"'{os.environ.get('AICORE_RESOURCE_GROUP')}':"
        )
        for deployment in deployments.resources:
            print(
                f"  - id={deployment.id}  scenario={getattr(deployment, 'scenario_id', None)}  "
                f"config={getattr(deployment, 'configuration_name', None)}  "
                f"url={getattr(deployment, 'deployment_url', None)}"
            )
        print(
            "\nIf you have a model deployment open in Launchpad, copy its URL "
            "into DIRECT_DEPLOYMENT_URL in config/config.json."
        )

    return deployments, client
