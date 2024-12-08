# stablecoin_usage.py - Example of stablecoin usage in transactions

class Stablecoin:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # Value in USD

    def convert_to_usd(self, amount):
        return amount * self.value

# Example usage
if __name__ == "__main__":
    usdt = Stablecoin("Tether", 1.0)  # 1 USDT = 1 USD
    amount = 50  # 50 USDT
    print(f"{amount} {usdt.name} is equivalent to ${usdt.convert_to_usd(amount)}")
