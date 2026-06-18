"""Load SAP AI Core credentials into environment variables."""

from __future__ import annotations

import json
import os
from pathlib import Path

TUTORIAL_ROOT = Path(__file__).resolve().parent.parent
LOCAL_CONFIG = TUTORIAL_ROOT / "config" / "config.json"
DEFAULT_CONFIG = Path.home() / ".aicore" / "config.json"

_ENV_KEYS = (
    "AICORE_AUTH_URL",
    "AICORE_CLIENT_ID",
    "AICORE_CLIENT_SECRET",
    "AICORE_RESOURCE_GROUP",
    "AICORE_BASE_URL",
    "ORCH_DEPLOYMENT_URL",
)


def _resolve_config_path(config_path: Path | None = None) -> Path:
    if config_path is not None:
        return config_path
    if LOCAL_CONFIG.exists():
        return LOCAL_CONFIG
    if DEFAULT_CONFIG.exists():
        return DEFAULT_CONFIG
    raise FileNotFoundError(
        "No AI Core config found. Copy config/config.example.json to config/config.json "
        "or create ~/.aicore/config.json with your service key values."
    )


def load_config(config_path: Path | None = None) -> dict:
    path = _resolve_config_path(config_path)
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def set_environment_variables(config_path: Path | None = None) -> dict:
    config = load_config(config_path)
    for key in _ENV_KEYS:
        value = config.get(key)
        if value:
            os.environ[key] = value

    base_url = os.environ.get("AICORE_BASE_URL", "")
    if base_url and not base_url.endswith("/v2"):
        os.environ["AICORE_BASE_URL"] = base_url.rstrip("/") + "/v2"

    auth_url = os.environ.get("AICORE_AUTH_URL", "")
    if auth_url and not auth_url.endswith("/oauth/token"):
        os.environ["AICORE_AUTH_URL"] = auth_url.rstrip("/") + "/oauth/token"

    return config


def load_registry_settings(config_path: Path | None = None) -> dict:
    path = config_path or (TUTORIAL_ROOT / "config" / "registry_settings.json")
    example = TUTORIAL_ROOT / "config" / "registry_settings.example.json"
    if not path.exists():
        if example.exists():
            path = example
        else:
            raise FileNotFoundError(
                "Copy config/registry_settings.example.json to config/registry_settings.json"
            )
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)
