# src/main/incentives/early_adopter_rewards.py

class EarlyAdopterRewards:
    def __init__(self):
        self.eligible_users = {}
        self.rewards = []

    def register_user(self, user_id, registration_date):
        """Register a user as an early adopter."""
        if user_id not in self.eligible_users:
            self.eligible_users[user_id] = registration_date
            print(f"User  {user_id} registered as an early adopter.")
        else:
            print(f"User  {user_id} is already registered.")

    def distribute_reward(self, user_id, reward):
        """Distribute a reward to an early adopter."""
        if user_id in self.eligible_users:
            self.rewards.append({'user_id': user_id, 'reward': reward})
            print(f"Distributed reward '{reward}' to user {user_id}.")
        else:
            print(f"User  {user_id} is not an eligible early adopter.")

    def get_rewards(self, user_id):
        """Get all rewards for a specific user."""
        return [r for r in self.rewards if r['user_id'] == user_id]

    def list_eligible_users(self):
        """List all eligible early adopters."""
        return list(self.eligible_users.keys())
