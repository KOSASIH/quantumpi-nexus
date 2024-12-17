# src/main/incentives/loyalty_program.py

class LoyaltyProgram:
    def __init__(self):
        self.user_points = {}
        self.rewards_catalog = {}

    def add_user(self, user_id):
        """Add a user to the loyalty program."""
        if user_id not in self.user_points:
            self.user_points[user_id] = 0
            print(f"User  {user_id} added to the loyalty program.")
        else:
            print(f"User  {user_id} is already in the loyalty program.")

    def add_points(self, user_id, points):
        """Add loyalty points to a user's account."""
        if user_id in self.user_points:
            self.user_points[user_id] += points
            print(f"Added {points} points to user {user_id}. Total points: {self.user_points[user_id]}")
        else:
            print(f"User  {user_id} is not in the loyalty program.")

    def redeem_points(self, user_id, points):
        """Redeem loyalty points for rewards."""
        if user_id in self.user_points:
            if self.user_points[user_id] >= points:
                self.user_points[user_id] -= points
                print(f"User  {user_id} redeemed {points} points. Remaining points: {self.user_points[user_id]}")
            else:
                print(f"User  {user_id} does not have enough points to redeem.")
        else:
            print(f"User  {user_id} is not in the loyalty program.")

    def add_reward(self, reward_name, points_required):
        """Add a reward to the rewards catalog."""
        self.rewards_catalog[reward_name] = points_required
        print(f"Reward '{reward_name}' added to the catalog with {points_required} points required.")

    def list_rewards(self):
        """List all available rewards."""
        return self.rewards_catalog
