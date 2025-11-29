import json

class InsightAgent:
    def analyze(self, weekly_stats):
        print("🧠 Insight Agent: Analyzing trends...")
        # Simulating LLM logic for the assignment submission
        # In a real scenario, this would call OpenAI API
        
        trends = weekly_stats[-1] # Get latest week
        return {
            "diagnosis": "ROAS has declined due to increasing CPMs.",
            "primary_driver": "Audience Fatigue",
            "confidence": 85,
            "evidence": f"Spend is {trends['spend']} but ROAS dropped to {round(trends['roas'], 2)}."
        }
