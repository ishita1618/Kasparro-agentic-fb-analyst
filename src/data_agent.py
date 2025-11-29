import pandas as pd
import numpy as np

class DataAgent:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        print("🤖 Data Agent: Loading data...")
        try:
            self.df = pd.read_csv(self.filepath)
            # Clean columns
            self.df.columns = [c.lower().replace(' ', '_') for c in self.df.columns]
            # Convert numbers
            for col in ['spend', 'revenue', 'impressions', 'clicks']:
                if col in self.df.columns:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0)
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def get_weekly_stats(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['week'] = self.df['date'].dt.to_period('W').astype(str)
        weekly = self.df.groupby('week').agg({
            'spend': 'sum', 'revenue': 'sum', 'impressions': 'sum', 'clicks': 'sum'
        }).reset_index()
        # KPI Calcs
        weekly['roas'] = np.where(weekly['spend']>0, weekly['revenue']/weekly['spend'], 0)
        weekly['ctr'] = np.where(weekly['impressions']>0, weekly['clicks']/weekly['impressions'], 0)
        return weekly.to_dict('records')

    def get_low_performing_ads(self):
        # Find ads with low CTR
        return self.df[self.df['clicks']/self.df['impressions'] < 0.015].head(5).to_dict('records')
