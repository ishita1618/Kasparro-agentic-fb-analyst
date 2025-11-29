# Kasparro Agentic Facebook Performance Analyst


An autonomous multi-agent system that diagnoses Facebook Ads performance, identifies reasons behind ROAS fluctuation, and recommends new creative directions.

# Architecture
1. Data Agent: Loads raw CSV, cleans data using Pandas, and aggregates metrics.
2. Insight Agent: Analyzes weekly trends to determine if drops are due to fatigue or scaling.
3. Creative Agent: Selects low-CTR ads and generates optimized copy variations.

# Structure
- `src/`: Contains the logic for all agents.
- `data/`: Synthetic dataset provided.
- `reports/`: Generated JSON and Markdown outputs from the agents.
- `run.py`: The main orchestrator script.

# How to Run
```bash
pip install -r requirements.txt
python run.py
