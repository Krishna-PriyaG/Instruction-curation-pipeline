from datasets import load_dataset
import pandas as pd

def fetch_sharegpt(output_path: str = "data/raw_sharegpt.jsonl", sample_size: int = 1000):
    print("Fetching ShareGPT dataset...")
    ds = load_dataset("anon8231489123/ShareGPT_Vicuna_unfiltered", split="train")
    df = pd.DataFrame(ds[:sample_size])
    df = df[["conversations"]]
    df.to_json(output_path, orient="records", lines=True)
    print(f"Saved {sample_size} samples to {output_path}")
