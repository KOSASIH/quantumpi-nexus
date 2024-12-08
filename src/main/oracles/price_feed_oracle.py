import requests
import time
import json
from statistics import mean
from threading import Thread, Event

class PriceFeedOracle:
    def __init__(self, sources, update_interval=60):
        self.sources = sources
        self.update_interval = update_interval
        self.price_data = {}
        self.stop_event = Event()

    def fetch_price(self, source):
        try:
            response = requests.get(source['url'])
            response.raise_for_status()
            data = response.json()
            price = data[source['price_key']]
            return price
        except Exception as e:
            print(f"Error fetching price from {source['name']}: {e}")
            return None

    def update_prices(self):
        while not self.stop_event.is_set():
            for source in self.sources:
                price = self.fetch_price(source)
                if price is not None:
                    self.price_data[source['name']] = price
            time.sleep(self.update_interval)

    def get_aggregated_price(self):
        if not self.price_data:
            return None
        return mean(self.price_data.values())

    def start(self):
        self.thread = Thread(target=self.update_prices)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()

# Example usage
if __name__ == "__main__":
    sources = [
        {'name': 'Exchange A', 'url': 'https://api.exchangeA.com/price', 'price_key': 'current_price'},
        {'name': 'Exchange B', 'url': 'https://api.exchangeB.com/price', 'price_key': 'latest_price'},
    ]
    
    oracle = PriceFeedOracle(sources)
    oracle.start()
    
    try:
        while True:
            aggregated_price = oracle.get_aggregated_price()
            print(f"Aggregated Price: {aggregated_price}")
            time.sleep(10)
    except KeyboardInterrupt:
        oracle.stop()
