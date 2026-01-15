"""
Extract and sample 100 reviews (50 positive, 50 negative) from the Sephora dataset.

Design principles:
- Reproducible sampling (fixed seed)
- Transparent filtering steps (print counts)
- Minimal assumptions about column names (try common alternatives)
- Keep review_text as close to raw as possible
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd


SEED_DEFAULT = 42
N_PER_CLASS_DEFAULT = 50
MAX_REVIEWS_PER_PRODUCT_DEFAULT = 3


def pick_first_existing_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    """Return the first column from candidates that exists in df, else None."""
    cols = set(df.columns)
    for c in candidates:
        if c in cols:
            return c
    return None


def normalize_rating(series: pd.Series) -> pd.Series:
    """Try to coerce rating to numeric."""
    return pd.to_numeric(series, errors="coerce")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to raw Sephora CSV file")
    parser.add_argument(
        "--output",
        default="luxury_reviews_100.csv",
        help="Output CSV filename (will be written to data/curated/)",
    )
    parser.add_argument("--seed", type=int, default=SEED_DEFAULT)
    parser.add_argument("--n_per_class", type=int, default=N_PER_CLASS_DEFAULT)
    parser.add_argument("--max_per_product", type=int, default=MAX_REVIEWS_PER_PRODUCT_DEFAULT)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] Input file not found: {input_path}")
        return 1

    # Load
    df = pd.read_csv(input_path)
    print(f"[INFO] Loaded rows: {len(df):,}")

    # Identify key columns (dataset-dependent naming)
    review_text_col = pick_first_existing_column(
        df,
        ["review_text", "review", "text", "reviewText", "ReviewText", "content"],
    )
    rating_col = pick_first_existing_column(
        df,
        ["rating", "stars", "score", "review_rating", "Rating"],
    )
    product_id_col = pick_first_existing_column(
        df,
        ["product_id", "productId", "product", "asin", "sku"],
    )
    product_name_col = pick_first_existing_column(
        df,
        ["product_name", "name", "productName", "ProductName", "title"],
    )
    language_col = pick_first_existing_column(
        df,
        ["language", "lang"],
    )

    if review_text_col is None or rating_col is None:
        print("[ERROR] Could not find required columns for review text and rating.")
        print(f"Available columns: {list(df.columns)}")
        return 1

    # Keep only rows with non-empty review text
    df = df.dropna(subset=[review_text_col])
    df[review_text_col] = df[review_text_col].astype(str).str.strip()
    df = df[df[review_text_col].str.len() > 0]
    print(f"[INFO] After non-empty text filter: {len(df):,}")

    # Optional language filter (English only)
    if language_col is not None:
        before = len(df)
        df[language_col] = df[language_col].astype(str).str.lower().str.strip()
        df = df[df[language_col].isin(["en", "english"])]
        print(f"[INFO] After language filter (English): {len(df):,} (dropped {before - len(df):,})")
    else:
        print("[INFO] No language column found; skipping language filter.")

    # Rating filter
    df[rating_col] = normalize_rating(df[rating_col])
    df = df.dropna(subset=[rating_col])
    df = df[(df[rating_col] <= 2) | (df[rating_col] >= 4)]  # exclude rating == 3 and other middles
    print(f"[INFO] After rating threshold filter (<=2 or >=4): {len(df):,}")

    # Deduplicate by exact review text
    before = len(df)
    df = df.drop_duplicates(subset=[review_text_col])
    print(f"[INFO] After dedup by text: {len(df):,} (dropped {before - len(df):,})")

    # Derive label
    df["label"] = df[rating_col].apply(lambda x: "positive" if x >= 4 else "negative")

    # Optional: cap reviews per product to reduce dominance
    if product_id_col is not None:
        before = len(df)
        df = (
            df.sort_values(by=[product_id_col, rating_col], ascending=[True, False])
            .groupby([product_id_col, "label"], as_index=False)
            .head(args.max_per_product)
        )
        print(
            f"[INFO] After per-product cap (max {args.max_per_product} per product per label): "
            f"{len(df):,} (dropped {before - len(df):,})"
        )
    else:
        print("[INFO] No product_id column found; skipping per-product cap.")

    # Sample balanced dataset
    pos = df[df["label"] == "positive"].sample(n=args.n_per_class, random_state=args.seed)
    neg = df[df["label"] == "negative"].sample(n=args.n_per_class, random_state=args.seed)
    sampled = pd.concat([pos, neg], ignore_index=True).sample(frac=1, random_state=args.seed).reset_index(drop=True)

    # Build curated dataframe with schema-aligned columns
    curated = pd.DataFrame(
        {
            "review_id": [f"sephora_{i:04d}" for i in range(1, len(sampled) + 1)],
            "review_text": sampled[review_text_col],
            "rating": sampled[rating_col].astype(int),
            "label": sampled["label"],
            "source": "sephora_kaggle",
            "language": "en",
        }
    )
    if product_id_col is not None:
        curated.insert(1, "product_id", sampled[product_id_col].astype(str))
    if product_name_col is not None:
        curated["product_name"] = sampled[product_name_col].astype(str)

    # Write output
    out_dir = Path("projects/sentiment-eval-prompt-strategies/data/curated")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / args.output
    curated.to_csv(out_path, index=False)
    print(f"[INFO] Wrote curated dataset: {out_path} ({len(curated):,} rows)")

    # Quick sanity checks
    print("[INFO] Label distribution:")
    print(curated["label"].value_counts())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
