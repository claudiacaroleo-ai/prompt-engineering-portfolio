# Runbook

I’m documenting the exact steps to reproduce the curated dataset used in this project.

My intent is to keep the repository lightweight and reproducible:
- raw data stays local (not committed to Git)
- the curated dataset can be regenerated deterministically using a fixed seed

## Prerequisites
- Python 3.10+
- `pandas` installed

## 1) Download the raw dataset
I download the “Sephora Products and Skincare Reviews” dataset from Kaggle and place the raw CSV file in:

`projects/sentiment-eval-prompt-strategies/data/raw/`

I keep this folder untracked by Git to avoid uploading large files or licensed data.

## 2) Run the sampling script
From the repository root, I run:

```bash
python projects/sentiment-eval-prompt-strategies/scripts/extract_and_sample.py \
  --input projects/sentiment-eval-prompt-strategies/data/raw/<YOUR_FILE_NAME>.csv \
  --output luxury_reviews_100.csv \
  --seed 42 \
  --n_per_class 50 \
  --max_per_product 3
```

## 3) Output
The script creates:
projects/sentiment-eval-prompt-strategies/data/curated/luxury_reviews_100.csv

## 4) Sanity checks
After generation, I verify:
- label distribution is 50/50
- review_text is non-empty
- duplicates are removed (by exact match)
- product dominance is reduced (if product_id is available)

If any of these checks fail, I revisit the sampling thresholds or the column mapping.
