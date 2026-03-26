# Setup Guide

Welcome to Dar Drip OS! This guide will help you get everything running in 10 minutes.

## Prerequisites

- Python 3.8 or higher
- Git (to clone this repo)
- Basic command line knowledge
- A text editor (VS Code recommended)

## Step 1: Clone the Repository

```bash
git clone https://github.com/DarDriper/dar-drip-os.git
cd dar-drip-os
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- pandas: For data management
- streamlit: For the dashboard
- python-dotenv: For environment variables

## Step 3: Set Up Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your preferences:
```
BRAND_NAME=Dar Drip
DATA_DIR=./data/raw
```

You don't need to change these unless you want to customize.

## Step 4: Verify Data Files

Check that these CSV files exist in `data/raw/`:
- `trend_radar.csv`
- `content_tracker.csv`
- `product_tracker.csv`
- `competitor_tracker.csv`
- `weekly_plan.csv`

They should already have demo data. You can start editing them right away!

## Step 5: Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Your browser will open automatically at `http://localhost:8501`

## What You'll See

The dashboard has 4 tabs:
1. **Overview**: Top priorities and scores
2. **Trends**: Trending topics to capitalize on
3. **Content**: Past performance analysis
4. **Products**: Product ideas ranked by potential

## Next Steps

- Read [usage.md](usage.md) to learn how to use each system
- Check out the [prompts/](../prompts/) folder for AI-assisted workflows
- Start replacing demo data with your real data

## Troubleshooting

### "Module not found"
Run `pip install -r requirements.txt` again

### "File not found"
Make sure you're in the `dar-drip-os` directory

### Dashboard won't load
Check that port 8501 isn't already in use

## Need Help?

Open an issue on GitHub or check the docs folder for more guides.
