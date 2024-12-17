# src/main/ai_integration/market_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

class MarketAnalysis:
    def __init__(self, api_url):
        self.api_url = api_url
        self.data = None

    def fetch_market_data(self):
        """Fetch market data from an external API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = pd.DataFrame(response.json())
            print("Market data fetched successfully.")
        else:
            raise Exception("Failed to fetch market data.")

    def analyze_trends(self):
        """Analyze market trends based on historical data."""
        if self.data is None:
            raise ValueError("Market data not available. Please fetch data first.")
        
        self.data['price_change'] = self.data['close'].pct_change()
        self.data['moving_average'] = self.data['close'].rolling(window=30).mean()
        
        print("Trend analysis completed.")
        return self.data[['timestamp', 'close', 'moving_average', 'price_change']]

    def visualize_trends(self):
        """Visualize market trends using matplotlib."""
        if self.data is None:
            raise ValueError("Market data not available. Please fetch data first.")
        
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['timestamp'], self.data['close'], label='Close Price', color='blue')
        plt.plot(self.data['timestamp'], self.data['moving_average'], label='30-Day Moving Average', color='orange')
        plt.title('Market Trends')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
