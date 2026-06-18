# Lesson 5: Prompt Engineering Techniques

**SAP Learning:** [Implementing Prompt Engineering Techniques](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/implementing-prompt-engineering-techniques)

**Notebook:** [notebooks/05_prompt_engineering.ipynb](../notebooks/05_prompt_engineering.ipynb)

## Few-shot prompting

Include labeled examples in the prompt so the model learns the expected output format and labeling style.

The notebook:

1. Samples 3 examples from the development set
2. Formats them as `<example>…</example>` blocks with input + JSON output
3. Evaluates **prompt_10** against the test set
4. Compares results to the lesson 4 baseline

## Meta-prompting

Use a stronger model (e.g. `gpt-4o`) to generate **classification guides** from labeled examples:

- `guide_urgency` — rules for high/medium/low
- `guide_sentiment` — rules for positive/negative/neutral
- `guide_categories` — rules per support category

These guides are injected into **prompt_12** and **prompt_13** for improved accuracy.

## Compare results

The notebook builds an `overall_result` table comparing:

- `basic--llama3.1-70b` (prompt_8)
- `few_shot--llama3.1-70b` (prompt_10)
- `meta_prompt--llama3.1-70b` (prompt_12/13)

## Next step

[06-multimodal.md](06-multimodal.md) — add image context to prompts.
