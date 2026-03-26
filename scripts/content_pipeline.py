"""
content_pipeline.py - Content Performance Pipeline for Dar Drip OS

How to use:
  1. Log your post results in data/raw/content.csv
  2. Run: python scripts/content_pipeline.py
  3. Output goes to data/processed/content_clean.csv
"""

import sys
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import (
    CONTENT_FILE, CONTENT_CLEAN_FILE, PROCESSED_DATA_DIR,
    WINNER_LABELS, WEAK_LABELS
)


def load_content():
    """Load the raw content CSV file."""
    if not CONTENT_FILE.exists():
        print(f"ERROR: Cannot find {CONTENT_FILE}")
        sys.exit(1)
    df = pd.read_csv(CONTENT_FILE)
    print(f"Loaded {len(df)} content entries.")
    return df


def clean_content(df):
    """Clean and enrich the content data."""
    df = df.copy()

    # Convert date column
    if "date_posted" in df.columns:
        df["date_posted"] = pd.to_datetime(df["date_posted"], errors="coerce")

    # Convert numeric columns
    numeric_cols = [
        "views_2h", "views_24h", "saves", "shares",
        "comments", "profile_visits", "dms", "orders"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Fill text columns
    for col in ["platform", "content_type", "hook", "format", "verdict", "notes"]:
        if col in df.columns:
            df[col] = df[col].fillna("")

    # Add engagement score: saves + shares + comments (weighted)
    if all(c in df.columns for c in ["saves", "shares", "comments"]):
        df["engagement_score"] = (
            df["saves"] * 3 +    # Saves are highest intent
            df["shares"] * 2 +   # Shares expand reach
            df["comments"] * 1   # Comments show connection
        )

    # Add view growth multiplier (24h views / 2h views)
    if all(c in df.columns for c in ["views_2h", "views_24h"]):
        df["view_growth"] = df.apply(
            lambda r: round(r["views_24h"] / r["views_2h"], 1)
            if r["views_2h"] > 0 else 0,
            axis=1
        )

    # Normalize verdict
    if "verdict" in df.columns:
        df["is_winner"] = df["verdict"].str.lower().isin(WINNER_LABELS)
        df["is_weak"] = df["verdict"].str.lower().isin(WEAK_LABELS)

    return df


def save_clean_content(df):
    """Save to processed folder."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CONTENT_CLEAN_FILE, index=False)
    print(f"Saved clean content to {CONTENT_CLEAN_FILE}")


def print_summary(df):
    """Print a quick content summary."""
    print("\n--- Content Performance Summary ---")
    print(f"Total posts logged: {len(df)}")

    if "is_winner" in df.columns:
        winners = df[df["is_winner"] == True]
        print(f"Winners: {len(winners)}")

    if "is_weak" in df.columns:
        weak = df[df["is_weak"] == True]
        print(f"Weak posts: {len(weak)}")

    if "engagement_score" in df.columns and len(df) > 0:
        top = df.loc[df["engagement_score"].idxmax()]
        print(f"Top engagement post: {top.get('hook', 'N/A')[:60]}...")

    if "format" in df.columns:
        best_format = df.groupby("format")["views_24h"].mean().idxmax()
        print(f"Best format by avg views: {best_format}")


def run():
    """Main entry point."""
    print("Running Content Pipeline...")
    df = load_content()
    df = clean_content(df)
    save_clean_content(df)
    print_summary(df)
    print("Done.")


if __name__ == "__main__":
    run()
