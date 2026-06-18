# SAP AI SDK Step-by-Step Tutorial

A linear, hands-on tutorial for **SAP Cloud SDK for AI (Python)** aligned with the SAP Learning course [Solve Your Business Problems Using Prompts and LLMs in SAP Generative AI Hub](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub).

This directory consolidates content that was previously spread across `09_BusinessAIWeek`, `10_Learning_Journeys`, and `11_orchestration` into one guided path.

## Business scenario

**Facility Solutions Company** receives high volumes of customer support mail. Your goal is to programmatically extract `urgency`, `sentiment`, and `categories` as structured JSON using the Generative AI Hub and Orchestration Service.

See [data/company-scope.md](data/company-scope.md) for the full scenario description.

## Prerequisites

Complete [docs/00-prerequisites.md](docs/00-prerequisites.md) before starting.

## Quick start

```bash
cd 12_sap_ai_sdk_tutorial
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp config/config.example.json config/config.json
# Edit config/config.json with your AI Core service key values
jupyter notebook notebooks/
```

## Tutorial path

| Step | Guide | Notebook | SAP Learning lesson |
|------|-------|----------|---------------------|
| 0 | [00-prerequisites.md](docs/00-prerequisites.md) | — | Setup |
| 1 | [01-sdk-setup.md](docs/01-sdk-setup.md) | [01_sdk_setup.ipynb](notebooks/01_sdk_setup.ipynb) | [Identifying the Need for SDK](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/identifying-the-need-for-using-sap-cloud-sdk-for-ai) |
| 2 | [02-orchestration.md](docs/02-orchestration.md) | [02_orchestration_translation.ipynb](notebooks/02_orchestration_translation.ipynb) | [Orchestration Services](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-interact-with-orchestration-services) |
| 3 | [03-prompt-development.md](docs/03-prompt-development.md) | [03_prompt_development.ipynb](notebooks/03_prompt_development.ipynb) | [Leverage the Power of LLMs](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-leverage-the-power-of-llms) |
| 4 | [04-prompt-evaluation.md](docs/04-prompt-evaluation.md) | [04_prompt_evaluation.ipynb](notebooks/04_prompt_evaluation.ipynb) | [Evaluate Prompts](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-evaluate-prompts) |
| 5 | [05-prompt-engineering.md](docs/05-prompt-engineering.md) | [05_prompt_engineering.ipynb](notebooks/05_prompt_engineering.ipynb) | [Prompt Engineering Techniques](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/implementing-prompt-engineering-techniques) |
| 6 | [06-multimodal.md](docs/06-multimodal.md) | [06_multimodal.ipynb](notebooks/06_multimodal.ipynb) | [Multimodal Input](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/enhancing-prompt-effectiveness-through-multi-modal-input) |
| 7 | [07-prompt-registry-launchpad.md](docs/07-prompt-registry-launchpad.md) | [07_prompt_registry.ipynb](notebooks/07_prompt_registry.ipynb) | Prompt Registry + Launchpad |

## Configuration

| File | Purpose |
|------|---------|
| `config/config.json` | AI Core credentials + optional `ORCH_DEPLOYMENT_URL` |
| `config/registry_settings.json` | Prompt Registry scenario/name/version (lesson 7) |

Copy the `*.example.json` files and fill in your values.

### Orchestration connection

The tutorial supports two modes (see [docs/02-orchestration.md](docs/02-orchestration.md)):

1. **Explicit URL** — set `ORCH_DEPLOYMENT_URL` in `config/config.json` from your Launchpad deployment
2. **Auto-detect** — leave `ORCH_DEPLOYMENT_URL` empty; the SDK finds a RUNNING orchestration deployment or creates one

## Package note

This tutorial installs `sap-ai-sdk-gen[all]`, the current name for the Python Generative AI SDK. The import path remains `gen_ai_hub`. The legacy PyPI name `generative-ai-hub-sdk` is the same package family.

## Disclaimer

Sample code for enablement only — not for production use.
