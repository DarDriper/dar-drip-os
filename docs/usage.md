# Usage Guide

This guide explains how to use each part of the Dar Drip OS.

## Daily Workflow

Here's a typical workflow for running Dar Drip:

**Morning (15 min)**
1. Open dashboard: `streamlit run dashboard/app.py`
2. Check Overview tab for top priorities
3. Note any urgent trends or high-scoring products

**During the day**
4. Create content based on insights
5. Log new trends, content, or product ideas as they come

**Evening (10 min)**
6. Update content_tracker.csv with today's post performance
7. Check what's trending on socials
8. Log any new observations

## Working with Each System

### 1. Trend Radar

**File:** `data/raw/trend_radar.csv`

**Purpose:** Track emerging trends in Moroccan streetwear and culture

**How to use:**
1. When you see something interesting, add a new row
2. Fill in: trend name, description, source, urgency, confidence
3. The system automatically scores it
4. Check dashboard to see top trends

**Tips:**
- Mark urgent trends (1-2 week window)
- High confidence = multiple signals
- Include specific examples in notes

### 2. Content Tracker

**File:** `data/raw/content_tracker.csv`

**Purpose:** Track what content performs well

**How to use:**
1. After posting, add a new row
2. Fill in: platform, content type, topic, engagement metrics
3. Dashboard shows which content types work best

**Tips:**
- Log ALL content, not just winners
- Be specific about topics
- Track both reach and engagement
- Use this to inform future content

### 3. Product Tracker

**File:** `data/raw/product_tracker.csv`

**Purpose:** Rank product ideas by potential

**How to use:**
1. When you have a product idea, add it
2. System scores based on: trend alignment, past success, feasibility
3. Dashboard ranks by total score

**Tips:**
- Be realistic about feasibility
- Consider production costs
- Link to relevant trends
- Track actual sales after launch

### 4. Competitor Tracker

**File:** `data/raw/competitor_tracker.csv`

**Purpose:** Monitor what competitors are doing

**How to use:**
1. When a competitor does something notable, log it
2. Track: what they did, how it performed, your takeaway
3. Use insights to differentiate

**Tips:**
- Don't copy - learn and differentiate
- Focus on 3-5 direct competitors
- Look for gaps they're missing

### 5. Weekly Planning

**File:** `data/raw/weekly_plan.csv`

**Purpose:** Plan your week's content and activities

**How to use:**
1. Every Sunday/Monday, review all data
2. Create 7-day content plan
3. Track execution during the week
4. Adjust as needed

**Tips:**
- Use the prompts folder for planning help
- Balance promotional vs. community content
- Leave room for spontaneous posts

## Using the Dashboard

### Overview Tab
- **Top Priority Trends:** Act on these ASAP
- **Top Product Ideas:** Consider launching these
- **Recent Content:** Your latest posts
- **This Week's Plan:** Your roadmap

### Trends Tab
- **All Trends:** Sorted by urgency and confidence
- **Filters:** Focus on specific types
- **Charts:** Visualize trend distribution

### Content Tab
- **Performance Analysis:** What's working?
- **By Platform:** Instagram vs. TikTok performance
- **By Type:** Reels vs. carousels vs. static

### Products Tab
- **Ranked Ideas:** Sorted by total score
- **Feasibility:** Can you actually make this?
- **Trend Link:** Which trends support this?

## Using AI Prompts

The `prompts/` folder has ready-to-use AI prompts:

1. **trend_discovery.md** - Find new trends
2. **content_analysis.md** - Analyze what worked
3. **product_ideation.md** - Generate product ideas
4. **competitor_research.md** - Research competitors
5. **weekly_planning.md** - Plan your week

**How to use:**
1. Open the prompt file
2. Copy the template
3. Fill in your data from CSV files
4. Paste into your AI tool (ChatGPT, Claude, etc.)
5. Use output to inform decisions

## Tips for Success

1. **Be consistent** - Log data regularly
2. **Be honest** - Track failures too
3. **Act on insights** - Don't just collect data
4. **Stay authentic** - Dar Drip is about culture, not trends alone
5. **Iterate** - Adjust scoring weights as you learn

## Advanced: Customizing Scores

Edit `scripts/config.py` to change how things are scored:

```python
TREND_WEIGHTS = {
    'urgency': 0.4,  # Increase for more urgency focus
    'confidence': 0.3,
    'cultural_fit': 0.3
}
```

Adjust based on what matters most to Dar Drip.
