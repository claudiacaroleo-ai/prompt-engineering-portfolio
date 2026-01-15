# Zero-shot baseline prompt

I use this prompt as a baseline to measure how well the model can perform binary sentiment classification without examples or domain-specific guidance.

## Prompt

Classify the sentiment of the following customer review as either **positive** or **negative**.

Return only one word: `positive` or `negative`.

Review:
{{review_text}}
