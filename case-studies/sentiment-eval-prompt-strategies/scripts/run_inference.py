import os
import csv
import time
from pathlib import Path

from openai import OpenAI

# --- Config (keep these aligned with your manual tests) ---
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1")  # Cambiato a modello esistente
_temp = os.getenv("OPENAI_TEMPERATURE", "0")  # Temperatura bassa per consistenza
TEMPERATURE = float(_temp) if _temp != "" else 0
MAX_OUTPUT_TOKENS = int(os.getenv("OPENAI_MAX_OUTPUT_TOKENS", "32"))

ROOT = Path(__file__).resolve().parents[1]  # .../sentiment-eval-prompt-strategies
PROMPTS_DIR = ROOT / "prompts"
DATA_DIR = ROOT / "data" / "curated"
RESULTS_DIR = ROOT / "results"

PROMPT_FILES = {
    "zero_shot": PROMPTS_DIR / "zero_shot.md",
    "few_shots_generic": PROMPTS_DIR / "few_shot_generic.md",
    "few_shots_failure_aware": PROMPTS_DIR / "few_shot_failure_aware.md",
}

DATASETS = {
    "hard_20": DATA_DIR / "hard_cases_20.csv",
}

def load_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()

def normalize_label(text: str) -> str:
    t = (text or "").strip().lower()
    if "positive" in t and "negative" not in t:
        return "positive"
    if "negative" in t and "positive" not in t:
        return "negative"
    # fallback: take first token
    first = t.split()[0] if t else ""
    return first if first in {"positive", "negative"} else ""

def run_strategy(client: OpenAI, dataset_path: Path, strategy_key: str, out_path: Path):
    prompt_text = load_prompt(PROMPT_FILES[strategy_key])

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with dataset_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    fieldnames = [
        "review_id",
        "true_label",
        "predicted_label",
        "strategy",
        "model",
        "notes",
        "raw_model_output",
    ]

    with out_path.open("w", encoding="utf-8", newline="") as wf:
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()

        for i, r in enumerate(rows, start=1):
            review_id = r.get("review_id") or r.get("id") or r.get("author_id") or str(i)
            review_text = r.get("review_text", "")
            true_label = r.get("label") or r.get("true_label") or ""

            # Usa l'API standard di OpenAI Chat Completions
            t0 = time.time()
            
            try:
                # Crea la richiesta usando chat.completions
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system", 
                            "content": prompt_text
                        },
                        {
                            "role": "user", 
                            "content": review_text
                        }
                    ],
                    max_tokens=MAX_OUTPUT_TOKENS,
                    temperature=TEMPERATURE,
                    # Aggiungi questi parametri per risultati più consistenti
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                
                # Estrai il testo dalla risposta
                raw = response.choices[0].message.content
                
            except Exception as e:
                print(f"Error processing review {review_id}: {e}")
                raw = ""
                # Se vuoi, puoi aggiungere una nota sull'errore
                notes = f"Error: {str(e)[:50]}"
            else:
                notes = ""

            pred = normalize_label(raw)
            if pred == "":
                notes = (notes + " | " if notes else "") + "parse_failed"

            writer.writerow({
                "review_id": review_id,
                "true_label": true_label,
                "predicted_label": pred,
                "strategy": strategy_key,
                "model": MODEL,
                "notes": notes,
                "raw_model_output": (raw or "").strip(),
            })

            dt_ms = int((time.time() - t0) * 1000)
            # Mostra più info nel log per debug
            print(f"[{strategy_key}] {i}/{len(rows)} id={review_id} true={true_label} pred={pred} raw='{(raw or '')[:30]}...' ({dt_ms} ms)")
            
            # Piccola pausa per evitare rate limiting (opzionale)
            if i % 10 == 0:
                time.sleep(0.5)

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENAI_API_KEY env var.")

    # Inizializza il client OpenAI
    client = OpenAI(api_key=api_key)
    
    # Test rapido della connessione
    print(f"Starting inference with model: {MODEL}")
    print(f"Temperature: {TEMPERATURE}")
    print(f"Max output tokens: {MAX_OUTPUT_TOKENS}")
    print("-" * 50)

    # Processa i dataset
    for dataset_name, dataset_path in DATASETS.items():
        if not dataset_path.exists():
            print(f"Warning: Dataset not found: {dataset_path}")
            continue
            
        print(f"\nProcessing dataset: {dataset_name}")
        
        for strategy_key in PROMPT_FILES.keys():
            prompt_path = PROMPT_FILES[strategy_key]
            if not prompt_path.exists():
                print(f"Warning: Prompt file not found: {prompt_path}")
                continue
                
            print(f"\nRunning strategy: {strategy_key}")
            out_file = RESULTS_DIR / f"predictions_{strategy_key}_auto__{dataset_name}.csv"
            
            try:
                run_strategy(client, dataset_path, strategy_key, out_file)
                print(f"✓ Completed {strategy_key} - Results saved to: {out_file}")
            except Exception as e:
                print(f"✗ Failed {strategy_key}: {e}")

    print("\n" + "=" * 50)
    print("All strategies completed!")

if __name__ == "__main__":
    main()