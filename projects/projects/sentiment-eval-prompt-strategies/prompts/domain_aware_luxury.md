# Domain-aware prompt (luxury beauty)

I use this prompt to evaluate how explicit domain context affects sentiment classification on luxury beauty reviews.

In this domain, sentiment is often expressed implicitly. Reviews may sound polite or neutral on the surface while still conveying dissatisfaction, especially when expectations around quality, performance, or value are not met.

## Prompt

You are classifying customer sentiment for luxury beauty products.

When determining sentiment, consider that:
- Negative sentiment may be expressed indirectly (e.g. disappointment, unmet expectations, subtle criticism).
- Positive sentiment often emphasizes satisfaction, perceived quality, or willingness to repurchase.
- Neutral or descriptive language should be interpreted in context, not in isolation.

Classify the sentiment of the following customer review as either **positive** or **negative**.

Return only one word: `positive` or `negative`.

Review:
{{review_text}}
