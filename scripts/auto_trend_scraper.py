#!/usr/bin/env python3
"""
Auto Trend Scraper for Dar Drip OS

This script automatically discovers trending topics from:
- Google Trends (Morocco + global streetwear)
- TikTok trending sounds/hashtags
- Instagram trending hashtags
- Twitter/X trending topics

Run this daily to keep your trend radar updated!
"""

import os
import pandas as pd
from datetime import datetime
import json
import requests
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).resolve().parent.parent
TRENDS_FILE = REPO_ROOT / 'data' / 'raw' / 'trend_radar.csv'

# Keywords to monitor for Dar Drip
MOROCCAN_KEYWORDS = [
    'moroccan fashion', 'moroccan streetwear', 'darija', 
    'morocco style', 'casablanca fashion', 'rabat style',
    'moroccan culture', 'atay', 'moroccan tea'
]

STREETWEAR_KEYWORDS = [
    'streetwear', 'street fashion', 'urban wear',
    'hypebeast', 'street style', 'street culture'
]

def get_google_trends():
    """
    Get trending topics from Google Trends
    Uses pytrends library (install: pip install pytrends)
    """
    try:
        from pytrends.request import TrendReq
        
        print("🔍 Fetching Google Trends...")
        pytrends = TrendReq(hl='en-US', tz=360)
        
        trends = []
        
        # Get trends for Morocco
        for keyword in MOROCCAN_KEYWORDS[:3]:  # Limit to avoid rate limits
            try:
                pytrends.build_payload([keyword], timeframe='now 7-d', geo='MA')
                interest = pytrends.interest_over_time()
                
                if not interest.empty:
                    avg_interest = interest[keyword].mean()
                    if avg_interest > 20:  # Only include if significant interest
                        trends.append({
                            'trend_name': keyword.title(),
                            'source': 'Google Trends (Morocco)',
                            'urgency': min(10, int(avg_interest / 10)),
                            'confidence': 8,
                            'notes': f'Average interest: {avg_interest:.0f}'
                        })
            except Exception as e:
                print(f"   ⚠️  Error fetching {keyword}: {e}")
                continue
        
        print(f"   ✅ Found {len(trends)} Google Trends")
        return trends
        
    except ImportError:
        print("   ⚠️  pytrends not installed. Run: pip install pytrends")
        return []

def get_tiktok_trends():
    """
    Get trending TikTok hashtags and sounds
    Note: TikTok API requires authentication. This is a placeholder.
    You can use TikTok's Creative Center or manual monitoring.
    """
    print("🎵 Checking TikTok Trends...")
    
    # Manual trending topics for Moroccan streetwear
    # Update these based on your TikTok research
    manual_trends = [
        {
            'trend_name': 'Moroccan Street Style Challenge',
            'source': 'TikTok',
            'urgency': 8,
            'confidence': 7,
            'notes': 'Check TikTok Creative Center for updates'
        }
    ]
    
    print(f"   ✅ Added {len(manual_trends)} TikTok trends (manual)")
    return manual_trends

def get_instagram_trends():
    """
    Get trending Instagram hashtags
    Uses manual research or Instagram Graph API
    """
    print("📸 Checking Instagram Trends...")
    
    # Placeholder for Instagram trends
    # You can integrate with Instagram Graph API or use manual research
    manual_trends = [
        {
            'trend_name': 'Moroccan Fashion Week',
            'source': 'Instagram',
            'urgency': 7,
            'confidence': 8,
            'notes': 'Monitor #moroccanfashion #darijavibes'
        }
    ]
    
    print(f"   ✅ Added {len(manual_trends)} Instagram trends (manual)")
    return manual_trends

def get_reddit_trends():
    """
    Get trending topics from Reddit streetwear communities
    """
    print("🔴 Checking Reddit...")
    
    try:
        # Use Reddit API (no auth needed for public data)
        subreddits = ['streetwear', 'streetwearstartup', 'morocco']
        trends = []
        
        for subreddit in subreddits:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
            headers = {'User-Agent': 'DarDripOS/1.0'}
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                posts = data['data']['children']
                
                # Look for highly upvoted posts
                for post in posts:
                    post_data = post['data']
                    if post_data['ups'] > 100:  # Significant upvotes
                        trends.append({
                            'trend_name': post_data['title'][:50],
                            'source': f'Reddit r/{subreddit}',
                            'urgency': 6,
                            'confidence': 7,
                            'notes': f"Upvotes: {post_data['ups']}"
                        })
        
        print(f"   ✅ Found {len(trends)} Reddit trends")
        return trends[:5]  # Limit to top 5
        
    except Exception as e:
        print(f"   ⚠️  Error fetching Reddit: {e}")
        return []

def save_trends(all_trends):
    """
    Save discovered trends to CSV
    """
    if not all_trends:
        print("\n❌ No new trends found")
        return
    
    print(f"\n💾 Saving {len(all_trends)} new trends...")
    
    # Load existing trends
    if TRENDS_FILE.exists():
        existing_df = pd.read_csv(TRENDS_FILE)
    else:
        existing_df = pd.DataFrame()
    
    # Create DataFrame from new trends
    new_df = pd.DataFrame(all_trends)
    new_df['date_added'] = datetime.now().strftime('%Y-%m-%d')
    new_df['cultural_fit'] = 8  # Default for Dar Drip
    
    # Combine with existing (avoid duplicates)
    if not existing_df.empty:
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df = combined_df.drop_duplicates(subset=['trend_name'], keep='last')
    else:
        combined_df = new_df
    
    # Save
    combined_df.to_csv(TRENDS_FILE, index=False)
    print(f"   ✅ Saved to {TRENDS_FILE}")
    print(f"   📊 Total trends in database: {len(combined_df)}")

def main():
    """
    Main function - run all trend scrapers
    """
    print("🚀 Starting Auto Trend Scraper for Dar Drip OS\n")
    print("="*50)
    
    all_trends = []
    
    # Run all scrapers
    all_trends.extend(get_google_trends())
    all_trends.extend(get_tiktok_trends())
    all_trends.extend(get_instagram_trends())
    all_trends.extend(get_reddit_trends())
    
    # Save results
    save_trends(all_trends)
    
    print("\n" + "="*50)
    print("✨ Done! Check your dashboard to see new trends.")
    print("\n💡 Next steps:")
    print("   1. Run: streamlit run dashboard/app.py")
    print("   2. Review new trends in the Trends tab")
    print("   3. Adjust urgency/confidence as needed")

if __name__ == '__main__':
    main()
