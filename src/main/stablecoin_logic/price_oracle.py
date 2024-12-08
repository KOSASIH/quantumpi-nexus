import requests
import numpy as np
from statistics import mean

class PriceOracle:
    def __init__(self, sources):
        self.sources = sources

    def fetch_price(self, source):
        try:
            response = requests.get(source)
            response.raise_for_status()
            return response.json()['price']
        except Exception as e:
            print(f"Error fetching price from {source}: {e}")
            return None

    def get_prices(self):
        prices = []
        for source in self.sources:
            price = self.fetch_price(source)
            if price is not None:
                prices.append(price)
        return prices

    def get_aggregated_price(self):
        prices = self.get_prices()
        if not prices:
            raise ValueError("No valid prices fetched.")
        
        # Use median to reduce the impact of outliers
        return np.median(prices)

# Example usage
if __name__ == "__main__":
    sources = [
        "https://api.exchange1.com/v1/ticker",
        "https://api.exchange2.com/v1/ticker",
        "https://api.exchange3.com/v1/ticker"
    ]
    oracle = PriceOracle(sources)
    print("Aggregated Price:", oracle.get_aggregated_price())
