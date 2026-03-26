"""
app.py - Dar Drip OS Dashboard

Run this with: streamlit run dashboard/app.py

Answers these questions:
- What is working?
- What is not working?
- What trend should I use next?
- Which content format is strongest?
- Which product idea deserves attention?
- What should I do this week?
"""

import sys
import streamlit as st
import pandas as pd
from pathlib import Path

# Add scripts to path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from config import (
    TRENDS_FILE, CONTENT_FILE, PRODUCTS_FILE,
    TRENDS_SCORED_FILE, CONTENT_CLEAN_FILE, PRODUCTS_SCORED_FILE
)

# ─── Config ──────────────────────────────────────────────────────────
st.set_page_config(page_title="Dar Drip OS", layout="wide", page_icon="🏛️")

# ─── Data Loading ──────────────────────────────────────────────────
@st.cache_data
def load_trends():
    if TRENDS_SCORED_FILE.exists():
        return pd.read_csv(TRENDS_SCORED_FILE)
    elif TRENDS_FILE.exists():
        return pd.read_csv(TRENDS_FILE)
    return pd.DataFrame()

@st.cache_data
def load_content():
    if CONTENT_CLEAN_FILE.exists():
        return pd.read_csv(CONTENT_CLEAN_FILE)
    elif CONTENT_FILE.exists():
        return pd.read_csv(CONTENT_FILE)
    return pd.DataFrame()

@st.cache_data
def load_products():
    if PRODUCTS_SCORED_FILE.exists():
        return pd.read_csv(PRODUCTS_SCORED_FILE)
    elif PRODUCTS_FILE.exists():
        return pd.read_csv(PRODUCTS_FILE)
    return pd.DataFrame()

trends_df = load_trends()
content_df = load_content()
products_df = load_products()

# ─── Header ─────────────────────────────────────────────────────────
st.title("🏛️ Dar Drip OS Dashboard")
st.markdown("**Your brand operating system for trends, content, and products.**")
st.divider()

# ─── KPI Row ──────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Trends Logged", len(trends_df))
with col2:
    st.metric("Posts Tracked", len(content_df))
with col3:
    st.metric("Product Ideas", len(products_df))
with col4:
    total_orders = int(content_df["orders"].sum()) if "orders" in content_df.columns else 0
    st.metric("Total Orders", total_orders)

st.divider()

# ─── Tabs ────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["**🔥 Trends**", "**📹 Content**", "**👕 Products**", "**✅ Actions**"])

# TAB 1: TRENDS
with tab1:
    st.subheader("Trend Leaderboard")
    if not trends_df.empty:
        display_cols = []
        for c in ["rank", "trend_name", "category", "dar_drip_fit_score", "total_score", "score_label"]:
            if c in trends_df.columns:
                display_cols.append(c)
        if display_cols:
            st.dataframe(trends_df[display_cols].head(10), use_container_width=True)
        else:
            st.dataframe(trends_df.head(10), use_container_width=True)
    else:
        st.info("No trends logged yet. Add trends to data/raw/trends.csv and run `python scripts/trend_pipeline.py`.")

# TAB 2: CONTENT
with tab2:
    st.subheader("Content Performance")
    if not content_df.empty:
        # Best hooks
        st.markdown("**Top 5 Hooks by Views**")
        content_sorted = content_df.copy()
        content_sorted["views_24h"] = pd.to_numeric(content_sorted.get("views_24h", 0), errors="coerce").fillna(0)
        top5 = content_sorted.nlargest(5, "views_24h")
        display_cols = []
        for c in ["hook", "format", "views_24h", "saves", "shares", "orders"]:
            if c in top5.columns:
                display_cols.append(c)
        st.dataframe(top5[display_cols], use_container_width=True)

        # Best format
        if "format" in content_df.columns:
            st.markdown("**Best Format by Avg Views**")
            format_stats = content_df.groupby("format")["views_24h"].mean().sort_values(ascending=False)
            st.bar_chart(format_stats)
    else:
        st.info("No content logged yet. Log your posts in data/raw/content.csv.")

# TAB 3: PRODUCTS
with tab3:
    st.subheader("Product Ideas")
    if not products_df.empty:
        display_cols = []
        for c in ["priority_rank", "idea_name", "phrase", "status", "interest_level", "orders", "priority_score"]:
            if c in products_df.columns:
                display_cols.append(c)
        if display_cols:
            st.dataframe(products_df[display_cols].head(10), use_container_width=True)
        else:
            st.dataframe(products_df.head(10), use_container_width=True)
    else:
        st.info("No product ideas yet. Add ideas to data/raw/products.csv.")

# TAB 4: ACTIONS
with tab4:
    st.subheader("✅ What to Do This Week")
    st.markdown("""
Use this checklist every Sunday to plan your week:

- **Check the Trend Leaderboard** → Pick the top trend and plan 3 posts around it.
- **Review Content Tab** → Repeat the winning hook format.
- **Review Products Tab** → Push the #1 ranked product this week.
- **Log last week's content** → Add your post results to data/raw/content.csv.
- **Generate Weekly Report** → Run `python scripts/weekly_report.py` to see what worked.
- **Update Weekly Plan** → Fill in data/raw/weekly_plan.csv with your content schedule.
    """)

    st.divider()
    st.markdown("### Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with col2:
        st.markdown("[View Reports →](../reports)")

st.divider()
st.caption("Dar Drip OS | Built for founders, not data scientists.")
