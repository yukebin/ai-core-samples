# Prerequisites

## SAP BTP and AI Core

1. SAP BTP subaccount with **SAP AI Core Extended Plan** (Generative AI Hub is not available on Free/Standard tiers)
2. SAP AI Core service instance and service key
3. SAP AI Launchpad connected to your AI Core instance
4. A **resource group** (not `default` for shared landscapes)

## Orchestration deployment

You need a RUNNING orchestration deployment before lessons 2–7.

**Option A — use your existing deployment (recommended):**

1. Open SAP AI Launchpad → **ML Operations** → **Deployments**
2. Find your orchestration deployment with status **RUNNING**
3. Copy the deployment URL into `config/config.json` as `ORCH_DEPLOYMENT_URL`

**Option B — create a new deployment:**

Follow [02-orchestration.md](02-orchestration.md) or the steps in [09_BusinessAIWeek/Test/07-deploy-orchestration-service.md](../../09_BusinessAIWeek/Test/07-deploy-orchestration-service.md).

## Local environment

- Python **3.11.9** or later
- Jupyter Notebook or JupyterLab
- Git clone of this repository

## Configuration files

```bash
cp config/config.example.json config/config.json
cp config/registry_settings.example.json config/registry_settings.json
```

Edit `config/config.json` with values from your AI Core service key:

| Key | Source |
|-----|--------|
| `AICORE_AUTH_URL` | Service key `url` (without `/oauth/token`; added automatically) |
| `AICORE_CLIENT_ID` | `clientid` |
| `AICORE_CLIENT_SECRET` | `clientsecret` |
| `AICORE_RESOURCE_GROUP` | Your resource group name |
| `AICORE_BASE_URL` | `serviceurls.AI_API_URL` + `/v2` |
| `ORCH_DEPLOYMENT_URL` | Deployment URL from Launchpad (optional) |

## Install dependencies

```bash
pip install -r requirements.txt
```

## Further reading

- [SAP AI Core setup](https://developers.sap.com/group.ai-core-get-started-basics.html)
- [Generative AI Hub documentation](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/generative-ai-hub-in-sap-ai-core-7db524ee75e74bf8b50c167951fe34a5)
