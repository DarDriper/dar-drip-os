"""
trend_pipeline.py - Trend Radar Pipeline for Dar Drip OS

How to use:
  1. Add rows to data/raw/trends.csv manually
  2. Run: python scripts/trend_pipeline.py
  3. Output goes to data/processed/trends_scored.csv

No scraping. No fake APIs. Just clean, honest data processing.
"""

import sys
import pandas as pd
from pathlib import Path

# Add scripts folder to Python path so we can import config and scoring
sys.path.insert(0, str(Path(__file__).parent))

from config import TRENDS_FILE, TRENDS_SCORED_FILE, PROCESSED_DATA_DIR
from scoring import score_trends_df


REQUIRED_COLUMNS = [
    "date_found", "source", "trend_name", "category",
    "short_description", "cultural_relevance_score",
    "dar_drip_fit_score", "content_potential_score",
    "product_potential_score", "notes"
]


def load_trends():
    """Load the raw trends CSV file."""
    if not TRENDS_FILE.exists():
        print(f"ERROR: Cannot find {TRENDS_FILE}")
        print("Please add your trends to data/raw/trends.csv first.")
        sys.exit(1)

    df = pd.read_csv(TRENDS_FILE)
    print(f"Loaded {len(df)} trends from {TRENDS_FILE.name}")
    return df


def validate_trends(df):
    """Check the data has the right columns and warn about missing values."""
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        print(f"WARNING: Missing columns: {missing_cols}")
        print("Your CSV may be outdated. Check the template in data/raw/trends.csv.")

    # Fill missing numeric scores with 0
    score_cols = [
        "cultural_relevance_score", "dar_drip_fit_score",
        "content_potential_score", "product_potential_score"
    ]
    for col in score_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Fill missing text fields with empty string
    for col in ["notes", "short_description", "source", "category"]:
        if col in df.columns:
            df[col] = df[col].fillna("")

    return df


def save_scored_trends(df):
    """Save the scored trends to the processed folder."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(TRENDS_SCORED_FILE, index=False)
    print(f"Saved scored trends to {TRENDS_SCORED_FILE}")


def print_summary(df):
    """Print a quick summary to the terminal."""
    print("\n--- Top 5 Trends for Dar Drip ---")
    top5 = df[["rank", "trend_name", "total_score", "score_label"]].head(5)
    print(top5.to_string(index=False))
    print("\nFull scored list saved to data/processed/trends_scored.csv")


def run():
    """Main entry point."""
    print("Running Trend Pipeline...")
    df = load_trends()
    df = validate_trends(df)
    df = score_trends_df(df)
    save_scored_trends(df)
    print_summary(df)
    print("Done.")


if __name__ == "__main__":
    run()
