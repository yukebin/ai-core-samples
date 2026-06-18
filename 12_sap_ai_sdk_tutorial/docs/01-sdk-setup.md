# Lesson 1: SDK Setup and Configuration

**SAP Learning:** [Identifying the Need for Using SAP Cloud SDK for AI](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/identifying-the-need-for-using-sap-cloud-sdk-for-ai)

**Notebook:** [notebooks/01_sdk_setup.ipynb](../notebooks/01_sdk_setup.ipynb)

## Why an SDK?

SAP AI Launchpad is ideal for interactive prompt development. To integrate LLM capabilities into applications at scale, you need programmatic access via the **SAP Cloud SDK for AI (Python)** — package name `sap-ai-sdk-gen`, import path `gen_ai_hub`.

SDK benefits:

- Accelerated development (auth, HTTP, model routing handled for you)
- Seamless integration into existing apps
- Programmatic access to templating, grounding, masking, and filtering

## Install

```bash
pip install "sap-ai-sdk-gen[all]"
```

The `[all]` extra includes LangChain and other optional integrations.

## Configure credentials

The SDK reads AI Core credentials from environment variables. This tutorial loads them from `config/config.json` via `src/init_env.py`.

Alternatively, use `~/.aicore/config.json` (see [00-prerequisites.md](00-prerequisites.md)).

## Verify connectivity

The notebook demonstrates:

1. Loading credentials
2. A **completion** call via `gen_ai_hub.proxy.native.openai.completions`
3. A **chat** call via `gen_ai_hub.proxy.native.openai.chat`

These confirm your Generative AI Hub connection before using Orchestration.

## Next step

[02-orchestration.md](02-orchestration.md) — interact with the Orchestration Service.
