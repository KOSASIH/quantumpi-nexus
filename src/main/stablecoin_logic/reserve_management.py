class ReserveManager:
    def __init__(self, total_supply, reserve_balance):
        self.total_supply = total_supply
        self.reserve_balance = reserve_balance

    def calculate_reserve_ratio(self):
        if self.total_supply == 0:
            raise ValueError("Total supply cannot be zero.")
        return self.reserve_balance / self.total_supply

    def maintain_reserve_ratio(self, target_ratio):
        current_ratio = self.calculate_reserve_ratio()
        if current_ratio < target_ratio:
            # Need to increase reserves
            return "Increase reserves by purchasing more assets."
        elif current_ratio > target_ratio:
            # Need to decrease reserves
            return "Decrease reserves by selling excess assets."
        else:
            return "Reserve ratio is optimal."

# Example usage
if __name__ == "__main__":
    total_supply = 1000000  # Total stablecoin supply
    reserve_balance = 950000  # Current reserve balance
    manager = ReserveManager(total_supply, reserve_balance)
    print("Current Reserve Ratio:", manager.calculate_reserve_ratio())
    print(manager.maintain_reserve_ratio(0.95))  # Target reserve ratio
