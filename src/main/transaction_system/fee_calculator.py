class FeeCalculator:
    def __init__(self, base_fee, volatility_factor):
        self.base_fee = base_fee
        self.volatility_factor = volatility_factor

    def calculate_fee(self, transaction_amount, network_conditions):
        # Adjust fee based on network conditions (e.g., congestion)
        congestion_multiplier = self.get_congestion_multiplier(network_conditions)
        fee = self.base_fee + (transaction_amount * self.volatility_factor) * congestion_multiplier
        return max(fee, self.base_fee)  # Ensure fee is at least the base fee

    def get_congestion_multiplier(self, network_conditions):
        # Placeholder for determining congestion multiplier
        if network_conditions == "high":
            return 2.0
        elif network_conditions == "medium":
            return 1.5
        else:
            return 1.0

# Example usage
if __name__ == "__main__":
    fee_calculator = FeeCalculator(base_fee=0.01, volatility_factor=0.001)
    transaction_amount = 100
    network_conditions = "high"  # Example condition
    fee = fee_calculator.calculate_fee(transaction_amount, network_conditions)
    print("Calculated Fee:", fee)
