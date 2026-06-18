# Lesson 7: Prompt Registry (Launchpad → SDK)

**Notebook:** [notebooks/07_prompt_registry.ipynb](../notebooks/07_prompt_registry.ipynb)

This lesson is not part of the original six SAP Learning modules. It closes the loop between **design-time** (SAP AI Launchpad) and **runtime** (your Python application).

## What is the Prompt Registry?

A centralized store for versioned prompt templates. Templates created in Launchpad can be retrieved and used programmatically — update the template in Launchpad and all consuming apps pick up the new version.

## Part A: Create template in SAP AI Launchpad

### 1. Open Prompt Editor

1. Open SAP AI Launchpad → **Generative AI Hub** → **Prompt Editor**

### 2. Configure metadata

| Field | Value |
|-------|-------|
| Name | `support-mail-classifier` |
| Collection | `facility-solutions` |
| Scenario | `facility-support` (note from Prompt Management after save) |
| Version | `1.0.0` |

### 3. Paste the prompt template

Use the consolidated prompt from lesson 3 (prompt_8). Include placeholders for runtime values:

```
You are an intelligent assistant. Extract and return a json with the following keys and values:
- "urgency" as one of {{?urgency}}
- "sentiment" as one of {{?sentiment}}
- "categories" list of the best matching support category tags from: {{?categories}}
Your complete message should be a valid json string that can be read directly and only contain the keys mentioned in the list above. Never enclose it in ```json...```, no newlines, no unnecessary whitespaces.

Giving the following message:
{{?input}}
```

### 4. Select model and parameters

1. Expand **Model and parameters**
2. Select a model (e.g. `gpt-4o`)
3. Set temperature and max tokens as needed

### 5. Save and verify

1. Click **Save**
2. Open **Generative AI Hub** → **Prompt Management**
3. Find `support-mail-classifier` under collection `facility-solutions`
4. Note the **scenario**, **name**, **version**, and **template ID**

### 6. Update local settings

Copy `config/registry_settings.example.json` to `config/registry_settings.json` and confirm values match your Launchpad template.

## Part B: Consume via SDK

The notebook uses **orchestration v2** and the Prompt Registry API:

1. `PromptTemplateClient.get_prompt_templates()` — verify the Launchpad template exists
2. `fill_prompt_template_by_id()` — preview filled prompt with runtime values
3. `OrchestrationService` with `TemplateRefByScenarioNameVersion` — run classification through your orchestration deployment using the registry template

```python
from gen_ai_hub.orchestration_v2 import (
    OrchestrationService,
    OrchestrationConfig,
    ModuleConfig,
    PromptTemplatingModuleConfig,
    LLMModelDetails,
    TemplateRefByScenarioNameVersion,
)

config = OrchestrationConfig(
    modules=ModuleConfig(
        prompt_templating=PromptTemplatingModuleConfig(
            prompt=TemplateRefByScenarioNameVersion(
                scenario="facility-support",
                name="support-mail-classifier",
                version="1.0.0",
            ),
            model=LLMModelDetails(name="gpt-4o"),
        )
    )
)

service = OrchestrationService(api_url=ORCH_DEPLOYMENT_URL, proxy_client=proxy_client)
result = service.run(
    config=config,
    placeholder_values={
        "input": mail["message"],
        "urgency": option_lists["urgency"],
        "sentiment": option_lists["sentiment"],
        "categories": option_lists["categories"],
    },
)
```

## Benefits

- **Centralized management** — prompt engineers work in Launchpad
- **Version control** — track and roll back template versions
- **No code changes** — update the template in Launchpad; apps reference scenario/name/version

## Further reading

- [Prompt Registry Python API](https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/prompt-registry.html)
- [Orchestration v2 API](https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html)
- [SAP tutorial: Prompt Registry](https://developers.sap.com/tutorials/ai-core-genaihub-prompt-registry.html)
