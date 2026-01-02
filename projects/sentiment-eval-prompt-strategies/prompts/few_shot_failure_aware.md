# Few-shot failure-aware prompt

I designed this few-shot prompt to explicitly address the main failure modes observed in the zero-shot baseline, such as implicit dissatisfaction, mixed sentiment, and expectation mismatch in luxury beauty reviews.

## Prompt

You are classifying customer sentiment based on written product reviews.

Classify each review as either **positive** or **negative**, considering the overall customer experience and whether expectations were met.

Return only one word: `positive` or `negative`.

### Examples

Review:
"I absolutely love how this feels and I use it every day."
Sentiment: positive

Review:
"The product did not work for me and I regret purchasing it."
Sentiment: negative

Review:
"It looks nice and feels pleasant, but I expected much better results."
Sentiment: negative

Review:
"The texture is great and the packaging is beautiful, but it didn’t actually improve anything."
Sentiment: negative

Review:
"It’s fine, but for the price I expected something more effective."
Sentiment: negative

### Review to classify:
{{review_text}}
