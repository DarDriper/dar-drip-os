"""
product_pipeline.py - Product Idea Pipeline for Dar Drip OS

How to use:
  1. Add ideas to data/raw/products.csv
  2. Run: python scripts/product_pipeline.py
  3. Output goes to data/processed/products_scored.csv
"""

import sys
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import PRODUCTS_FILE, PRODUCTS_SCORED_FILE, PROCESSED_DATA_DIR
from scoring import score_products_df


def load_products():
    """Load product ideas from CSV."""
    if not PRODUCTS_FILE.exists():
        print(f"ERROR: Cannot find {PRODUCTS_FILE}")
        sys.exit(1)
    df = pd.read_csv(PRODUCTS_FILE)
    print(f"Loaded {len(df)} product ideas.")
    return df


def clean_products(df):
    """Clean and validate product data."""
    df = df.copy()

    # Fill numeric fields
    if "orders" in df.columns:
        df["orders"] = pd.to_numeric(df["orders"], errors="coerce").fillna(0)

    # Fill text fields
    text_cols = [
        "idea_name", "phrase", "product_type", "category",
        "concept_description", "design_direction", "status",
        "tested", "interest_level", "repeat_potential", "notes"
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("")

    return df


def save_scored_products(df):
    """Save to processed folder."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PRODUCTS_SCORED_FILE, index=False)
    print(f"Saved scored products to {PRODUCTS_SCORED_FILE}")


def print_summary(df):
    """Print product summary."""
    print("\n--- Top Product Ideas ---")
    cols = ["priority_rank", "idea_name", "phrase", "priority_score", "status", "orders"]
    available = [c for c in cols if c in df.columns]
    print(df[available].head(5).to_string(index=False))


def run():
    """Main entry point."""
    print("Running Product Pipeline...")
    df = load_products()
    df = clean_products(df)
    df = score_products_df(df)
    save_scored_products(df)
    print_summary(df)
    print("Done.")


if __name__ == "__main__":
    run()
