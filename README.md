# Dar Drip OS

> The operating system for Dar Drip — a Moroccan streetwear brand built on culture, Darija, tea rituals, and identity.

---

## What is Dar Drip OS?

Dar Drip OS is a lightweight system that helps you run your brand like a pro every week.
No complicated tech. No data science degree needed.
Just open it, fill in what happened, and let it tell you what to do next.

**It helps you:**
- Log and score trends from TikTok, Google Trends, and Meta
- Track how your content is performing (Reels, TikToks, posts)
- Track product and drop ideas with clear statuses
- Log what competitors are doing and what you can steal
- Plan your weekly content calendar
- Generate a weekly report in plain language
- Run a dashboard that answers: What is working? What is not? What should I do this week?

---

## Folder Structure

```
dar-drip-os/
├─ README.md                  ← This file
├─ requirements.txt           ← Python packages to install
├─ .env.example               ← Environment config template
├─ .gitignore                 ← Files Git should ignore
├─ data/
│  ├─ raw/                    ← YOUR input files (edit these manually)
│  └─ processed/              ← Auto-generated cleaned + scored files
├─ scripts/                   ← All Python scripts
├─ dashboard/                 ← Streamlit dashboard app
├─ reports/                   ← Auto-generated weekly reports land here
├─ prompts/                   ← AI prompt templates for Dar Drip
├─ docs/                      ← Full documentation
└─ .github/workflows/         ← GitHub automation
```

---

## Quick Start (Step by Step)

### Step 1: Clone the repo
```bash
git clone https://github.com/DarDriper/dar-drip-os.git
cd dar-drip-os
```

### Step 2: Install Python packages
```bash
pip install -r requirements.txt
```

### Step 3: Add your data
- Open `data/raw/trends.csv` and log your trends
- Open `data/raw/content.csv` and log your content results
- Open `data/raw/products.csv` and log your product ideas

### Step 4: Run the pipelines
```bash
python scripts/trend_pipeline.py
python scripts/content_pipeline.py
python scripts/product_pipeline.py
```

### Step 5: Generate a weekly report
```bash
python scripts/weekly_report.py
```
Your report will appear in `/reports/`.

### Step 6: Run the dashboard
```bash
streamlit run dashboard/app.py
```
Open your browser at `http://localhost:8501`

---

## Systems Overview

| System | File | What it does |
|---|---|---|
| Trend Radar | `data/raw/trends.csv` | Log trends with scores |
| Content Tracker | `data/raw/content.csv` | Log post performance |
| Product Tracker | `data/raw/products.csv` | Track drop ideas |
| Competitor Log | `data/raw/competitors.csv` | Log competitor posts |
| Weekly Planner | `data/raw/weekly_plan.csv` | Plan your week |
| Weekly Report | `scripts/weekly_report.py` | Generate markdown report |
| Dashboard | `dashboard/app.py` | Visual overview |

---

## Documentation

See the `/docs` folder for full guides:
- [Getting Started](docs/getting_started.md)
- [Data Guide](docs/data_guide.md)
- [Reports and Dashboard](docs/reports_and_dashboard.md)
- [GitHub Actions](docs/github_actions.md)

---

## Brand Context

**Dar Drip** is a Moroccan streetwear brand built around:
- Darija phrases and cultural humor
- Moroccan tea rituals and daily habits
- Identity-driven, shareable streetwear
- Premium feel with local roots

This OS is built specifically for Dar Drip decision-making.

---

## Tech Stack

- Python 3.10+
- pandas
- Streamlit
- CSV / JSON data storage
- GitHub Actions for automation
- Markdown reports

---

*Built for founders, not data scientists. Simple, actionable, and Moroccan.*
