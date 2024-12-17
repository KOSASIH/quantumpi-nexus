# src/tests/test_incentives.py

import unittest
from main.incentives import EarlyAdopterRewards, LoyaltyProgram

class TestIncentives(unittest.TestCase):
    def setUp(self):
        self.early_adopter_rewards = EarlyAdopterRewards()
        self.loyalty_program = LoyaltyProgram()

    def test_register_user(self):
        self.early_adopter_rewards.register_user("user123", "2023-01-01")
        self.assertIn("user123", self.early_adopter_rewards.eligible_users)

    def test_distribute_reward(self):
        self.early_adopter_rewards.register_user("user123", "2023-01-01")
        self.early_adopter_rewards.distribute_reward("user123", "Free Gift")
        rewards = self.early_adopter_rewards.get_rewards("user123")
        self.assertEqual(len(rewards), 1)
        self.assertEqual(rewards[0]['reward'], "Free Gift")

    def test_get_rewards_no_rewards(self):
        self.early_adopter_rewards.register_user("user123", "2023-01-01")
        rewards = self.early_adopter_rewards.get_rewards("user456")  # User not registered
        self.assertEqual(rewards, [])

    def test_add_user_loyalty_program(self):
        self.loyalty_program.add_user("user123")
        self.assertIn("user123", self.loyalty_program.user_points)

    def test_add_points(self):
        self.loyalty_program.add_user("user123")
        self.loyalty_program.add_points("user123", 50)
        self.assertEqual(self.loyalty_program.user_points["user123"], 50)

    def test_redeem_points(self):
        self.loyalty_program.add_user("user123")
        self.loyalty_program.add_points("user123", 100)
        self.loyalty_program.redeem_points("user123", 50)
        self.assertEqual(self.loyalty_program.user_points["user123"], 50)

    def test_redeem_points_insufficient(self):
        self.loyalty_program.add_user("user123")
        self.loyalty_program.add_points("user123", 30)
        with self.assertRaises(ValueError):
            self.loyalty_program.redeem_points("user123", 50)

    def test_add_reward(self):
        self.loyalty_program.add_reward("10% Off", 100)
        self.assertIn("10% Off", self.loyalty_program.rewards_catalog)

    def test_list_rewards(self):
        self.loyalty_program.add_reward("10% Off", 100)
        self.loyalty_program.add_reward("Free Shipping", 50)
        rewards = self.loyalty_program.list_rewards()
        self.assertEqual(len(rewards), 2)

if __name__ == '__main__':
    unittest.main()
