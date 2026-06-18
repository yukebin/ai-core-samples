# Lesson 3: Prompt Development

**SAP Learning:** [Using SAP Cloud SDK for AI to Leverage the Power of LLMs](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-leverage-the-power-of-llms)

**Notebook:** [notebooks/03_prompt_development.ipynb](../notebooks/03_prompt_development.ipynb)

## Scenario

Classify incoming support mail for **Facility Solutions Company**. Extract:

- `urgency` — `low`, `medium`, `high`
- `sentiment` — `positive`, `negative`, `neutral`
- `categories` — from the company-defined list in [data/service-categories.md](../data/service-categories.md)

## Dataset

The notebook loads `data/filtered_mails-hardest.jsonl` — synthetic mails with ground-truth labels for evaluation.

## Iterative prompt refinement

| Step | Goal |
|------|------|
| prompt_1 | Basic extraction (unstructured output) |
| prompt_2 | Constrain urgency/sentiment to allowed values |
| prompt_3 | Request JSON output |
| prompt_4 | Clean JSON (no markdown fences, no extra whitespace) |
| prompt_5–7 | Add category classification with constrained values |
| prompt_8 | **Combined** prompt — production-ready JSON with all three fields |

Each step uses `send_request()` from `src/send_request.py`, which routes through your orchestration deployment.

## Key insight

Prompt development is iterative. Start simple, add constraints, enforce output format, then combine into one application-ready prompt.

## Next step

[04-prompt-evaluation.md](04-prompt-evaluation.md) — measure prompt quality on a dataset.
