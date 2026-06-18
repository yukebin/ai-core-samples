# Lesson 4: Prompt Evaluation

**SAP Learning:** [Using SAP Cloud SDK for AI to Evaluate Prompts](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/using-sap-cloud-sdk-for-ai-to-evaluate-prompts)

**Notebook:** [notebooks/04_prompt_evaluation.ipynb](../notebooks/04_prompt_evaluation.ipynb)

## Why evaluate?

A prompt that works on one mail may fail at scale. Automated evaluation establishes a baseline and tracks improvements.

## Metrics

For each mail, the evaluator checks:

| Metric | Description |
|--------|-------------|
| `is_valid_json` | Response parses as JSON |
| `correct_urgency` | Matches ground truth |
| `correct_sentiment` | Matches ground truth |
| `correct_categories` | Overlap score vs ground-truth category set |

## Implementation

`src/evaluation.py` provides:

- `evaluation()` — score a single mail
- `evalulation_full_dataset()` — run across a dataset with rate limiting
- `pretty_print_table()` — display results

## Baseline

The notebook evaluates **prompt_8** (combined prompt from lesson 3) on a 20-mail test subset. Expect non-deterministic LLM output — rerun results may vary.

Typical baseline (llama3.1-70b):

```
                    is_valid_json correct_categories correct_sentiment correct_urgency
basic--llama3.1-70b        100.0%              83.5%             30.0%           70.0%
```

## Next step

[05-prompt-engineering.md](05-prompt-engineering.md) — improve the baseline with few-shot and meta-prompting.
