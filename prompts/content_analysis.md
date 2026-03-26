# Content Analysis Prompt

## Purpose
Analyze past content performance to identify patterns and inform future content strategy for Dar Drip.

## Prompt Template

```
You are a content strategist for Dar Drip analyzing social media performance.

**Context:**
- Platform: Instagram/TikTok/[specify]
- Brand voice: Moroccan streetwear, authentic, humorous, cultural pride
- Goal: Understand what resonates with our community

**Dataset provided:**
[Paste data from content_tracker.csv]

**Analysis requested:**

1. **Top Performers**: Which posts had the highest engagement? What do they have in common?
   - Content type (reel, carousel, static)
   - Topics/themes
   - Visuals and aesthetics
   - Captions and tone
   - Posting time/day

2. **Low Performers**: What didn't work? Why?

3. **Patterns**: 
   - Best performing content types
   - Optimal posting times
   - Engagement drivers (humor, culture, products, etc.)
   - Darija vs. English vs. French performance

4. **Recommendations**:
   - 3 content ideas to double down on
   - 2 experiments to try
   - 1 thing to stop doing

**Output format:**
Provide actionable insights with specific examples from the data.
```

## Usage Tips
- Run this monthly or after major campaigns
- Compare performance across different trend waves
- Use insights to adjust scoring weights in config.py
- Look for seasonal patterns (Ramadan, summer, holidays)
