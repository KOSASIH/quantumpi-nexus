import numpy as np

class VolatilityManager:
    def __init__(self, price_history):
        self.price_history = price_history

    def calculate_volatility(self):
        if len(self.price_history) < 2:
            raise ValueError("Not enough data to calculate volatility.")
        
        returns = np.diff(self.price_history) / self.price_history[:-1]
        volatility = np.std(returns)
        return volatility

    def adjust_supply(self, current_price, target_price):
        volatility = self.calculate_volatility()
        adjustment_factor = 1 + volatility  # Adjust supply based on volatility

        if current_price < target_price:
            # Increase supply
            return adjustment_factor
        else:
            # Decrease supply
            return 1 / adjustment_factor

# Example usage
if __name__ == "__main__":
    price_history = [1.00, 1.02, 0.98, 1.01, 1.03]
    manager = VolatilityManager(price_history)
    print("Current Volatility:", manager.calculate_volatility())
    print("Supply Adjustment Factor:", manager.adjust_supply(1.01, 1.00))
