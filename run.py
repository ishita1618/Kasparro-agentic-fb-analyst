import yaml
import json
import os
from src.data_agent import DataAgent
from src.insight_agent import InsightAgent
from src.creative_agent import CreativeAgent

# Load Config
try:
    with open("config/config.yaml") as f:
        cfg = yaml.safe_load(f)
except:
    # Fallback if config file issues
    cfg = {"paths": {"data": "data/synthetic_fb_ads_undergarments.csv", "reports": "reports/"}}

def main():
    # Setup
    os.makedirs("reports", exist_ok=True)
    
    # 1. Data
    data_agent = DataAgent(cfg['paths']['data'])
    if not data_agent.load_data():
        print("Data file not found!")
        return

    # 2. Insights
    stats = data_agent.get_weekly_stats()
    insight_agent = InsightAgent()
    insights = insight_agent.analyze(stats)
    
    with open("reports/insights.json", "w") as f:
        json.dump(insights, f, indent=4)

    # 3. Creatives
    bad_ads = data_agent.get_low_performing_ads()
    creative_agent = CreativeAgent()
    new_creatives = creative_agent.rewrite_ads(bad_ads)
    
    with open("reports/creatives.json", "w") as f:
        json.dump(new_creatives, f, indent=4)

    # 4. Final Report
    with open("reports/report.md", "w") as f:
        f.write(f"# Analysis Report\n\n**Diagnosis:** {insights['diagnosis']}\n")

    print("✅ Agent System Finished Successfully.")

if __name__ == "__main__":
    main()
