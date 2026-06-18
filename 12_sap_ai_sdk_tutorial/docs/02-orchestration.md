# Lesson 2: Orchestration Service

**SAP Learning:** [Using SAP Cloud SDK for AI to Interact with Orchestration Services](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-interact-with-orchestration-services)

**Notebook:** [notebooks/02_orchestration_translation.ipynb](../notebooks/02_orchestration_translation.ipynb)

## What is Orchestration?

The Orchestration Service chains modules — templating, LLM, grounding, masking, content filtering — into a single endpoint. You deploy orchestration once and access all configured models through it.

## Deploy in SAP AI Launchpad

If you do not already have a RUNNING orchestration deployment:

1. Open **ML Operations** → **Configurations** → **Create**
2. Name: `orchestration-conf`
3. Scenario: `orchestration`, executable: `orchestration`
4. Review and create
5. Click **Create Deployment**, set duration to **standard**
6. Wait until status is **RUNNING**
7. Copy the deployment URL

Paste the URL into `config/config.json`:

```json
"ORCH_DEPLOYMENT_URL": "https://your-deployment-url..."
```

## Connect from Python

`src/orchestration_helper.py` resolves the deployment URL:

| Mode | Behavior |
|------|----------|
| `ORCH_DEPLOYMENT_URL` set | Uses your Launchpad deployment directly |
| Not set | Auto-detects a RUNNING orchestration deployment |
| None found | Creates configuration + deployment (fallback) |

## Orchestration workflow (SDK)

1. Initialize `OrchestrationService` with your deployment URL
2. Define a `Template` with system/user messages and `{{?placeholders}}`
3. Define an `LLM` (model name, temperature, max_tokens)
4. Create `OrchestrationConfig` combining template + LLM
5. Call `run()` with `TemplateValue` inputs

The notebook runs a **translation assistant** example from the SAP Learning course.

## Next step

[03-prompt-development.md](03-prompt-development.md) — iterative prompt development for support mail classification.
