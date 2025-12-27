# Dataset schema

I’m defining the dataset schema before sampling any data to keep the experiment honest and reproducible.

My goal is to compare prompt strategies, not to “tune” the dataset around a specific prompt. By locking the schema first, I make sure:
- I know exactly what information is available to the prompt and to the evaluation
- I can regenerate the same dataset later (or ask someone else to reproduce it)
- I avoid accidental leakage (e.g., product-related shortcuts) that could inflate results

## Output file

I will produce a single curated file:

- `luxury_reviews_100.csv`

## Columns

### Required
- `review_id`  
  A stable identifier for each row in the curated dataset. If the source dataset has an ID, I’ll use it; otherwise I’ll generate one.

- `review_text`  
  The raw review text I will send to the model. I keep it as close as possible to the original to preserve real-world noise.

- `rating`  
  The numeric rating from the source dataset. I will use this to derive labels (positive/negative) with clear thresholds.

- `label`  
  The ground-truth label for evaluation:
  - `positive` if rating ≥ 4  
  - `negative` if rating ≤ 2  
  (I will exclude rating == 3 to avoid ambiguous cases in a binary setup.)

- `source`  
  A short string to track provenance, e.g. `sephora_kaggle`.

- `language`  
  I expect English reviews in this subset, so this will be `en`.  
  If I later expand cross-lingually, I can extend this field without changing the schema.

- `language`  
  I expect English reviews in this subset, so this will be `en`.  
  If I later expand cross-lingually, I can extend this field without changing the schema.

### Optional (used to reduce sampling bias)
- `product_id`  
  If available, I’ll keep a product identifier to control sampling so that one product doesn’t dominate the dataset.

- `product_name`  
  Helpful for interpretation and error analysis, but not required for running the evaluation.

## Notes on what the model will see

In the experiments, the model will only see `review_text`.  
I keep fields like `rating`, `label`, and product metadata for evaluation and analysis only.

This separation is intentional: it helps me reason clearly about what information is driving performance (prompt design vs hidden shortcuts in the data).
