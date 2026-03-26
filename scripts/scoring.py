"""
scoring.py - Scoring logic for Dar Drip OS

This file calculates scores for trends and products.
Scores are based on weighted logic - no fake AI, just clear math.
You can change the weights in config.py.
"""

import pandas as pd
from config import TREND_SCORING_WEIGHTS


def score_trend_row(row):
    """
    Calculate a total score for a single trend row.
    Uses weighted average of the scoring columns.
    Score range: 0 to 10.

    Weights (configured in config.py):
    - Dar Drip Fit:       30%
    - Cultural Relevance: 25%
    - Content Potential:  20%
    - Product Potential:  15%
    - Intuition Bonus:    10% (based on notes length as a proxy)
    """
    score = 0.0

    # Add weighted scores from each column
    for col, weight in TREND_SCORING_WEIGHTS.items():
        try:
            value = float(row.get(col, 0))
            score += value * weight
        except (ValueError, TypeError):
            pass  # Skip if value is missing or not a number

    # Intuition bonus: if notes exist and are meaningful, add up to 1 point
    notes = str(row.get("notes", ""))
    intuition_bonus = min(len(notes) / 50, 1.0)  # Max 1 point bonus
    score += intuition_bonus * 1.0 * 0.10  # 10% weight on a 10-point scale

    return round(score, 2)


def score_trends_df(df):
    """
    Apply scoring to all trends in a DataFrame.
    Adds a 'total_score' column and sorts by score descending.
    """
    df = df.copy()

    # Calculate score for each trend
    df["total_score"] = df.apply(score_trend_row, axis=1)

    # Add a rank column (1 = best trend)
    df = df.sort_values("total_score", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1

    # Add a simple label for quick reading
    df["score_label"] = df["total_score"].apply(label_score)

    return df


def label_score(score):
    """
    Convert a numeric score to a human-readable label.
    """
    if score >= 8.5:
        return "Top Priority"
    elif score >= 7.0:
        return "Strong"
    elif score >= 5.5:
        return "Average"
    elif score >= 4.0:
        return "Weak"
    else:
        return "Skip"


def score_product_row(row):
    """
    Calculate a priority score for a product idea.
    Based on interest_level + orders + repeat_potential.
    """
    score = 0.0

    # Interest level mapping
    interest_map = {"high": 10, "medium": 5, "low": 2}
    score += interest_map.get(str(row.get("interest_level", "")).lower(), 0) * 0.40

    # Orders (normalize to 10-point scale, max assumed 100 orders)
    try:
        orders = float(row.get("orders", 0))
        score += min(orders / 10, 10) * 0.40
    except (ValueError, TypeError):
        pass

    # Repeat potential
    repeat_map = {"yes": 10, "no": 0, "unknown": 4}
    score += repeat_map.get(str(row.get("repeat_potential", "")).lower(), 0) * 0.20

    return round(score, 2)


def score_products_df(df):
    """
    Apply scoring to all product ideas in a DataFrame.
    """
    df = df.copy()
    df["priority_score"] = df.apply(score_product_row, axis=1)
    df = df.sort_values("priority_score", ascending=False).reset_index(drop=True)
    df["priority_rank"] = df.index + 1
    return df
