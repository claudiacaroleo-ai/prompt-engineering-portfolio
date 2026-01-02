# Results schema

Before running any evaluations, I define how prediction results will be recorded.

This helps keep predictions, metrics, and qualitative analysis clearly separated.

## Per-strategy prediction files

For each prompt strategy, I will generate a CSV file named:

`predictions_<strategy>.csv`

Each file will contain one row per review with the following fields:

- `review_id`  
  Identifier linking predictions back to the curated dataset.

- `review_text`  
  The original review text used as model input.

- `true_label`  
  Ground-truth label derived from rating thresholds.

- `predicted_label`  
  Model output (`positive` or `negative`).

- `strategy`  
  Prompt strategy used for this prediction (e.g. `zero_shot`, `few_shot`, `domain_aware`).

- `model`  
  Model identifier used for the run.

- `notes`  
  Optional field for manual observations during error analysis.
