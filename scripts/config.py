"""
config.py - Central configuration for Dar Drip OS

All paths and settings live here.
Change values in this file to adjust the system.
"""

import os
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

# Root of the project (one level up from /scripts)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"

# Output folders
REPORTS_DIR = ROOT_DIR / "reports"

# Input CSV files
TRENDS_FILE = RAW_DATA_DIR / "trends.csv"
CONTENT_FILE = RAW_DATA_DIR / "content.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "products.csv"
COMPETITORS_FILE = RAW_DATA_DIR / "competitors.csv"
WEEKLY_PLAN_FILE = RAW_DATA_DIR / "weekly_plan.csv"

# Processed output files
TRENDS_SCORED_FILE = PROCESSED_DATA_DIR / "trends_scored.csv"
CONTENT_CLEAN_FILE = PROCESSED_DATA_DIR / "content_clean.csv"
PRODUCTS_SCORED_FILE = PROCESSED_DATA_DIR / "products_scored.csv"
COMPETITORS_CLEAN_FILE = PROCESSED_DATA_DIR / "competitors_clean.csv"
WEEKLY_PLAN_CLEAN_FILE = PROCESSED_DATA_DIR / "weekly_plan_clean.csv"

# ─── Scoring Weights ─────────────────────────────────────────────────────────
# These control how trend scores are calculated.
# All weights must add up to 1.0 (100%)
# Change these numbers to prioritize different factors.

TREND_SCORING_WEIGHTS = {
    "dar_drip_fit_score": 0.30,       # 30% - How well this trend fits Dar Drip
    "cultural_relevance_score": 0.25, # 25% - How relevant to Moroccan culture
    "content_potential_score": 0.20,  # 20% - How strong for content
    "product_potential_score": 0.15,  # 15% - How strong for products
    # 10% is reserved for intuition bonus (notes-based)
}

# ─── Content Verdict Labels ───────────────────────────────────────────────────
# These are the allowed values for the 'verdict' column in content.csv
WINNER_LABELS = ["winner", "top performer"]
WEAK_LABELS = ["weak", "flop"]

# ─── Brand Info ───────────────────────────────────────────────────────────────
BRAND_NAME = os.getenv("BRAND_NAME", "Dar Drip")

# ─── Ensure folders exist ────────────────────────────────────────────────────
def ensure_dirs():
    """Create all needed folders if they don't exist yet."""
    for d in [RAW_DATA_DIR, PROCESSED_DATA_DIR, REPORTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure_dirs()
    print("Dar Drip OS - Directories verified.")
