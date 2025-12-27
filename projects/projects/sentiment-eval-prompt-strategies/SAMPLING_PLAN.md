# Sampling plan (v1)

I will work with a total of 100 English-language reviews, evenly balanced across sentiment:
- 50 positive reviews (rating ≥ 4)
- 50 negative reviews (rating ≤ 2)

Reviews with a rating of 3 are excluded, as they tend to express mixed or ambiguous sentiment and would introduce noise into a binary classification task.

## Sampling rules
- I will randomly sample reviews using a fixed random seed to ensure reproducibility.
- I will remove duplicate review texts to avoid over-representing repeated content.
- Reviews will be kept largely “as-is”, with minimal cleaning, to preserve real-world language variability and noise.
