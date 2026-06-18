# Lesson 6: Multimodal Input

**SAP Learning:** [Enhancing Prompt Effectiveness Through Multi-modal Input](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/enhancing-prompt-effectiveness-through-multi-modal-input)

**Notebook:** [notebooks/06_multimodal.ipynb](../notebooks/06_multimodal.ipynb)

## Why multimodal?

A short complaint plus a photo of damage gives the LLM much richer context than text alone. Multimodal models (e.g. GPT-4o) accept both text and images.

## Try in SAP AI Launchpad (no code)

1. Open **Generative AI Hub** → **Prompt Editor**
2. Enter a short support mail and classification instructions
3. Click **Upload Image** to attach a photo
4. Compare JSON output with and without the image

## Programmatic approach

The notebook extends `send_request()` to support `ImageUrlContent` alongside `TextContent` in orchestration `UserMessage` content parts.

Requirements:

- A multimodal model deployed (e.g. `gpt-4o`)
- A publicly accessible image URL the model can fetch

## Evaluation

Use the same evaluation functions from lesson 4 to confirm multimodal input improves classification accuracy.

## Next step

[07-prompt-registry-launchpad.md](07-prompt-registry-launchpad.md) — centralize prompts in Launchpad and consume via SDK.
