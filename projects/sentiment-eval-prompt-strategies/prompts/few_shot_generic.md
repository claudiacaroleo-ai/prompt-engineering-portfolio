# Few-shot generic prompt

I use this prompt to evaluate how a small number of generic examples affects sentiment classification performance, without introducing any domain-specific framing.

## Prompt

Classify the sentiment of the following customer review as either **positive** or **negative**.

Here are some examples:

Review:
"The product works exactly as described and I am very satisfied with the quality."
Sentiment: positive

Review:
"I was disappointed by the performance and would not buy this again."
Sentiment: negative

Review:
"Shipping was fast and the item exceeded my expectations."
Sentiment: positive

Review:
"The product did not deliver the results I expected and I would not purchase it again."
Sentiment: negative

Now classify the following review.

Return only one word: `positive` or `negative`.

Review:
{{review_text}}
