class CreativeAgent:
    def rewrite_ads(self, bad_ads):
        print("🎨 Creative Agent: Writing new ads...")
        recommendations = []
        
        for ad in bad_ads:
            recommendations.append({
                "original": ad.get('creative_message', 'N/A'),
                "new_version": "🔥 Limited Time: 50% Off Best Sellers! Shop Now.",
                "reasoning": "Added urgency and a clear offer."
            })
        return recommendations
