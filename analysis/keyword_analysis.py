"""
Beliefs in Wreaths - Google Ads Keyword Analysis
Analyzes keyword performance and identifies optimization opportunities
"""

import pandas as pd
import os
from datetime import datetime

def load_keyword_report(filepath):
    """Load the keyword report CSV, skipping header rows"""
    df = pd.read_csv(filepath, skiprows=2)
    # Remove summary rows at the bottom
    df = df[df['Keyword status'].notna() & (df['Keyword status'] != '--')]
    return df

def analyze_performance(df):
    """Perform comprehensive performance analysis"""
    
    print("=" * 80)
    print("BELIEFS IN WREATHS - GOOGLE ADS KEYWORD ANALYSIS")
    print("=" * 80)
    print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Report Period: 19 September 2025 - 2 October 2025")
    
    # Overall metrics
    print("\n" + "=" * 80)
    print("OVERALL CAMPAIGN PERFORMANCE")
    print("=" * 80)
    total_keywords = len(df)
    total_impr = df['Impr.'].sum()
    total_clicks = df['Clicks'].sum()
    total_cost = df['Cost'].sum()
    avg_ctr = (total_clicks / total_impr * 100) if total_impr > 0 else 0
    avg_cpc = (total_cost / total_clicks) if total_clicks > 0 else 0
    
    print(f"Total Keywords: {total_keywords}")
    print(f"Total Impressions: {int(total_impr)}")
    print(f"Total Clicks: {int(total_clicks)}")
    print(f"Average CTR: {avg_ctr:.2f}%")
    print(f"Total Cost: AUD ${total_cost:.2f}")
    print(f"Average CPC: AUD ${avg_cpc:.2f}")
    print(f"Conversions: {df['Conversions'].sum():.0f}")
    
    # Ad Group Performance
    print("\n" + "=" * 80)
    print("PERFORMANCE BY AD GROUP")
    print("=" * 80)
    ad_group_perf = df.groupby('Ad group').agg({
        'Keyword': 'count',
        'Impr.': 'sum',
        'Clicks': 'sum',
        'Cost': 'sum',
        'Conversions': 'sum'
    }).round(2)
    ad_group_perf.columns = ['Keywords', 'Impressions', 'Clicks', 'Cost (AUD)', 'Conversions']
    ad_group_perf['CTR %'] = ((ad_group_perf['Clicks'] / ad_group_perf['Impressions'] * 100)
                               .fillna(0).round(2))
    print(ad_group_perf.to_string())
    
    # Status Analysis
    print("\n" + "=" * 80)
    print("KEYWORD STATUS BREAKDOWN")
    print("=" * 80)
    status_counts = df['Status'].value_counts()
    print(status_counts.to_string())
    
    # Paused keywords
    paused = df[df['Status reasons'].str.contains('paused', na=False)]
    print(f"\n⚠️  CRITICAL: {len(paused)} keywords are PAUSED (All Year Products)")
    
    # Low quality keywords
    low_quality = df[df['Status reasons'].str.contains('low quality', na=False)]
    if len(low_quality) > 0:
        print(f"⚠️  WARNING: {len(low_quality)} keywords have LOW QUALITY SCORE:")
        for idx, row in low_quality.iterrows():
            print(f"   - {row['Keyword']} ({row['Ad group']})")
    
    # Match Type Analysis
    print("\n" + "=" * 80)
    print("MATCH TYPE DISTRIBUTION")
    print("=" * 80)
    match_type_dist = df.groupby(['Match type', 'Status']).size().unstack(fill_value=0)
    print(match_type_dist.to_string())
    
    # Active keywords with traffic
    print("\n" + "=" * 80)
    print("ACTIVE KEYWORDS WITH TRAFFIC (Eligible + Impressions > 0)")
    print("=" * 80)
    active_traffic = df[(df['Status'] == 'Eligible') & (df['Impr.'] > 0)].copy()
    active_traffic = active_traffic.sort_values('Clicks', ascending=False)
    
    if len(active_traffic) > 0:
        print(f"\n{len(active_traffic)} keywords generating traffic:\n")
        for idx, row in active_traffic.iterrows():
            ctr = row['CTR'].replace('%', '') if isinstance(row['CTR'], str) else row['CTR']
            print(f"✓ '{row['Keyword']}' ({row['Match type']})")
            print(f"  Impressions: {int(row['Impr.'])} | Clicks: {int(row['Clicks'])} | "
                  f"CTR: {ctr} | Cost: AUD ${row['Cost']:.2f}")
    else:
        print("⚠️  No active keywords with traffic!")
    
    # Problem Keywords
    print("\n" + "=" * 80)
    print("PROBLEM KEYWORDS TO REVIEW")
    print("=" * 80)
    
    # Generic/irrelevant keywords
    generic_keywords = [
        'gift for', 'best present', 'best gift', 'cool gifts',
        'birthday ideas for women', 'birthday ideas for her',
        'best birthday gift ideas', 'best birthday presents',
        'good birthday gift ideas', 'great birthday gift ideas',
        'fun gift idea', 'good gift idea', 'gift idea for',
        'Black Friday Sale', 'EOFY Sale'
    ]
    
    print("\n🚫 GENERIC/IRRELEVANT KEYWORDS (NOT WREATH-SPECIFIC):")
    found_generic = df[df['Keyword'].isin(generic_keywords)]
    if len(found_generic) > 0:
        for keyword in found_generic['Keyword'].unique():
            print(f"   ❌ {keyword}")
    
    # Too broad keywords
    print("\n⚠️  OVERLY BROAD KEYWORDS (High risk of irrelevant traffic):")
    broad_keywords = df[(df['Match type'] == 'Broad Match') & 
                        (df['Keyword'].str.len() < 15) &
                        (df['Status'] == 'Eligible')]
    if len(broad_keywords) > 0:
        for keyword in broad_keywords['Keyword'].unique():
            if keyword not in generic_keywords:
                print(f"   ⚠️  {keyword}")
    
    return df

def generate_recommendations(df):
    """Generate actionable recommendations"""
    
    print("\n" + "=" * 80)
    print("IMMEDIATE ACTION ITEMS")
    print("=" * 80)
    
    recommendations = []
    
    # Check paused ad group
    paused = df[df['Status reasons'].str.contains('paused', na=False)]
    if len(paused) > 0:
        print("\n🔴 PRIORITY 1: UNPAUSE 'ALL YEAR PRODUCTS' AD GROUP")
        print("   - Currently ALL 27 keywords in this ad group are inactive")
        print("   - These are your core wreath keywords")
        print("   - Action: Review budget and unpause the ad group")
        recommendations.append("Unpause 'All Year Products' ad group")
    
    # Low impression volume
    print("\n🔴 PRIORITY 2: INCREASE BIDS/BUDGET")
    print("   - Only 36 total impressions in 2 weeks is extremely low")
    print("   - Top performing keyword 'luxury christmas wreath australia' only 5 impressions")
    print("   - Action: Increase daily budget or keyword bids by 50-100%")
    recommendations.append("Increase daily budget to at least $20-30/day")
    recommendations.append("Increase bids on top keywords to $1.50-2.00")
    
    # Remove generic keywords
    print("\n🔴 PRIORITY 3: REMOVE IRRELEVANT KEYWORDS")
    print("   - 15+ generic gift/birthday keywords waste budget")
    print("   - Not relevant to wreath products")
    print("   - Action: Pause or delete these keywords immediately")
    recommendations.append("Remove all generic gift and birthday keywords")
    
    # Add negative keywords
    print("\n🟡 PRIORITY 4: ADD NEGATIVE KEYWORDS")
    print("   - Prevent irrelevant clicks on broad match terms")
    print("   - Suggested negatives: diy, tutorial, how to make, funeral, sympathy")
    recommendations.append("Add negative keyword list")
    
    # Conversion tracking
    print("\n🟡 PRIORITY 5: SET UP CONVERSION TRACKING")
    print("   - Currently 0 conversions tracked")
    print("   - Cannot measure ROI without tracking")
    print("   - Action: Install Google Ads conversion tag on thank you page")
    recommendations.append("Implement conversion tracking")
    
    # Match type optimization
    print("\n🟡 PRIORITY 6: OPTIMIZE MATCH TYPES")
    print("   - Too many broad match keywords (79% of keywords)")
    print("   - Add more Exact and Phrase match for better control")
    recommendations.append("Add exact match versions of top performers")
    
    return recommendations

def generate_new_keyword_suggestions():
    """Generate wreath-focused keyword suggestions"""
    
    print("\n" + "=" * 80)
    print("RECOMMENDED NEW KEYWORDS TO ADD")
    print("=" * 80)
    
    print("\n🎯 HIGH-INTENT PURCHASE KEYWORDS (Exact Match):")
    exact_keywords = [
        "[buy wreath online australia]",
        "[premium door wreaths australia]",
        "[luxury door wreath]",
        "[designer wreath australia]",
        "[front door wreath sydney]",
        "[front door wreath melbourne]",
        "[handmade wreath australia]",
        "[eucalyptus wreath australia]",
        "[artificial wreath australia]"
    ]
    for kw in exact_keywords:
        print(f"   {kw}")
    
    print("\n🎯 PRODUCT-SPECIFIC KEYWORDS (Phrase Match):")
    phrase_keywords = [
        '"eucalyptus door wreath"',
        '"native australian wreath"',
        '"all season wreath"',
        '"year round door wreath"',
        '"premium artificial wreath"',
        '"designer door decoration"',
        '"luxury home decor wreath"'
    ]
    for kw in phrase_keywords:
        print(f"   {kw}")
    
    print("\n🎯 SEASONAL KEYWORDS (For Christmas campaign):")
    seasonal_keywords = [
        '"christmas door wreath australia"',
        '[buy christmas wreath online]',
        '"luxury christmas door decoration"',
        '[designer christmas wreath australia]',
        '"premium christmas wreaths sydney"'
    ]
    for kw in seasonal_keywords:
        print(f"   {kw}")

def main():
    """Main analysis function"""
    
    # Update this path to your actual file location
    csv_path = r"c:\Users\vsetc\Downloads\Search keyword report.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: File not found at {csv_path}")
        print("Please update the csv_path variable in the script.")
        return
    
    # Load and analyze data
    df = load_keyword_report(csv_path)
    analyze_performance(df)
    recommendations = generate_recommendations(df)
    generate_new_keyword_suggestions()
    
    # Summary
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print("\nNext Steps:")
    print("1. Review the priority actions above")
    print("2. Check the ACTION-PLAN.md file for detailed implementation steps")
    print("3. Request access to Google Ads account for direct changes")
    print("4. Get search terms report to see actual queries triggering ads")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
