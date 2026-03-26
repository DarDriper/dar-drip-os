# Testing Guide for Dar Drip OS

This guide will help you test the system step-by-step to make sure everything works.

## ✅ Quick Test (5 minutes)

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/DarDriper/dar-drip-os.git
cd dar-drip-os
```

### Step 2: Check Python Version

Make sure you have Python 3.8 or higher:

```bash
python --version
# or
python3 --version
```

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
# or if pip doesn't work:
pip3 install -r requirements.txt
```

This will install:
- pandas (for data handling)
- streamlit (for the dashboard)
- python-dotenv (for configuration)

### Step 4: Test the Dashboard

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

Your browser should automatically open to `http://localhost:8501`

**What you should see:**
- ✅ 4 tabs: Overview, Trends, Content, Products
- ✅ Demo data already loaded
- ✅ Charts and tables displaying
- ✅ No errors in the terminal

### Step 5: Test the Scripts

Test each Python script individually:

**Test scoring:**
```bash
python scripts/scoring.py
```
Should complete without errors.

**Test trend pipeline:**
```bash
python scripts/trend_pipeline.py
```
Should create `data/processed/trend_radar_scored.csv`

**Test content pipeline:**
```bash
python scripts/content_pipeline.py
```
Should create `data/processed/content_tracker_scored.csv`

**Test product pipeline:**
```bash
python scripts/product_pipeline.py
```
Should create `data/processed/product_tracker_scored.csv`

**Test weekly report:**
```bash
python scripts/weekly_report.py
```
Should create a markdown file in `reports/weekly_report_YYYY-MM-DD.md`

## 🔍 Detailed Testing

### Test 1: Verify Data Files

Check that all CSV files exist:

```bash
ls -la data/raw/
```

You should see:
- trend_radar.csv
- content_tracker.csv
- product_tracker.csv
- competitor_tracker.csv
- weekly_plan.csv

### Test 2: Read Data Files

Open Python and test reading the data:

```python
import pandas as pd

# Test loading trend data
trends = pd.read_csv('data/raw/trend_radar.csv')
print(f"Loaded {len(trends)} trends")
print(trends.head())

# Test loading content data
content = pd.read_csv('data/raw/content_tracker.csv')
print(f"Loaded {len(content)} content items")
print(content.head())

# Test loading product data
products = pd.read_csv('data/raw/product_tracker.csv')
print(f"Loaded {len(products)} products")
print(products.head())
```

All should load without errors.

### Test 3: Test Scoring System

Open Python and test the scoring functions:

```python
from scripts.scoring import score_trend, score_content, score_product

# Test trend scoring
trend_score = score_trend(
    urgency=8,
    confidence=9,
    cultural_fit=10
)
print(f"Trend score: {trend_score}")
# Should output a number between 0-10

# Test content scoring  
content_score = score_content(
    reach=5000,
    engagement_rate=0.08,
    saves=150,
    shares=75
)
print(f"Content score: {content_score}")
# Should output a number

# Test product scoring
product_score = score_product(
    trend_alignment=8,
    past_success=7,
    feasibility=9,
    market_demand=8
)
print(f"Product score: {product_score}")
# Should output a number between 0-10
```

### Test 4: Test Dashboard Features

With the dashboard running (`streamlit run dashboard/app.py`):

1. **Overview Tab:**
   - ✅ See "Top Priority Trends" section
   - ✅ See "Top Product Ideas" section
   - ✅ See "Recent Content" section
   - ✅ See "This Week's Plan" section

2. **Trends Tab:**
   - ✅ See all trends in a table
   - ✅ Trends sorted by urgency
   - ✅ See urgency and confidence metrics

3. **Content Tab:**
   - ✅ See content performance table
   - ✅ See charts for different platforms
   - ✅ See engagement metrics

4. **Products Tab:**
   - ✅ See product ideas ranked by score
   - ✅ See trend alignment
   - ✅ See feasibility ratings

### Test 5: Test AI Prompts

1. Open `prompts/trend_discovery.md`
2. Copy the prompt template
3. Test it with ChatGPT or Claude
4. Should give you structured trend analysis

Repeat for all 5 prompt files.

### Test 6: Test Weekly Report

After running `python scripts/weekly_report.py`:

1. Check `reports/` folder
2. Open the generated markdown file
3. Should contain:
   - Week summary
   - Top trends
   - Best performing content
   - Top product ideas
   - Recommendations

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "FileNotFoundError"

**Solution:** Make sure you're in the `dar-drip-os` directory:
```bash
pwd
# Should show: /path/to/dar-drip-os
```

### Issue: Dashboard won't load

**Solution:** Check if port 8501 is already in use:
```bash
streamlit run dashboard/app.py --server.port 8502
```

### Issue: "Permission denied"

**Solution (Mac/Linux):**
```bash
chmod +x scripts/*.py
```

### Issue: CSV encoding errors

**Solution:** Make sure CSV files are saved with UTF-8 encoding

## ✨ Success Checklist

If all of these work, your system is 100% functional:

- [ ] Repository cloned successfully
- [ ] Dependencies installed
- [ ] Dashboard runs and opens in browser
- [ ] All 4 tabs display data
- [ ] trend_pipeline.py runs without errors
- [ ] content_pipeline.py runs without errors
- [ ] product_pipeline.py runs without errors
- [ ] weekly_report.py generates a report
- [ ] Processed CSV files created in data/processed/
- [ ] Report created in reports/ folder

## 🚀 Next Steps

Once everything works:

1. Replace demo data with your real Dar Drip data
2. Start logging trends, content, and products
3. Run the dashboard weekly to get insights
4. Use the AI prompts for strategy planning
5. Customize scoring weights in `scripts/config.py`

## 📞 Need Help?

If you encounter issues:

1. Check error messages carefully
2. Make sure Python 3.8+ is installed
3. Try reinstalling dependencies
4. Check file paths are correct
5. Open an issue on GitHub with error details

---

**Built for Dar Drip 🇲🇦**

Moroccan streetwear deserves a system that works as smooth as your Darija flows.
