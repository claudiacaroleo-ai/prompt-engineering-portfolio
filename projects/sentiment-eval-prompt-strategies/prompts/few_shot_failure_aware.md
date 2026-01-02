## Prompt

You are classifying customer sentiment from luxury beauty product reviews.

Classify each review as **positive** or **negative** based on the overall experience and whether expectations were met.

Decision rules (important):
- If the reviewer expresses disappointment, unmet expectations, regret, or “would not repurchase”, classify as **negative** even if the tone is polite.
- If sentiment is mixed, choose the label that matches the final takeaway (repurchase intent, recommendation, or overall satisfaction).
- Praising packaging/texture/scent does NOT override negative outcomes (no results, irritation, breakouts, dryness, wasting money).

Return only one word: `positive` or `negative`.

### Examples

Review:
"I love the texture and I keep repurchasing it — my skin feels noticeably better."
Sentiment: positive

Review:
"At first it felt nice, but after a week it irritated my skin and I stopped using it."
Sentiment: negative

Review:
"It smells great and the packaging is beautiful, but it didn’t actually improve anything."
Sentiment: negative

Review:
"It’s fine, but for the price I expected something more effective. I wouldn’t buy it again."
Sentiment: negative

Review:
"Not dramatic, but it consistently keeps my skin comfortable and I’d recommend it to friends."
Sentiment: positive

### Review to classify:
{{review_text}}