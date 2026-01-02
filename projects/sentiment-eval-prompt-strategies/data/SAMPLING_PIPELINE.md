# Sampling pipeline

Before writing any code, I define the sampling pipeline step by step to make the process transparent and reproducible.

This pipeline reflects the sequence of decisions I apply when moving from the raw Sephora dataset to the final curated sample used for prompt evaluation.

## Pipeline steps

1. Load the raw Sephora reviews dataset.

2. Keep only English-language reviews, if a language field is available in the source data.

3. Filter reviews by rating:
   - keep reviews with rating ≥ 4 (positive candidates)
   - keep reviews with rating ≤ 2 (negative candidates)
   - exclude reviews with rating == 3 to avoid ambiguous sentiment

4. Deduplicate reviews by exact `review_text` match to prevent repeated content from skewing results.

5. If product identifiers are available, limit the number of reviews per product to reduce dominance from a single item.

6. Randomly sample:
   - 50 positive reviews
   - 50 negative reviews
   using a fixed random seed for reproducibility.

7. Derive the `label` field from the rating thresholds.

8. Export the final dataset to `luxury_reviews_100.csv` for use in prompt evaluation.
