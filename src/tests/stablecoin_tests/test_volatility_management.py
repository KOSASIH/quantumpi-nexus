import unittest
from src.main.stablecoin.volatility_management import VolatilityManagement

class TestVolatilityManagement(unittest.TestCase):

    def setUp(self):
        self.vm = VolatilityManagement()

    def test_calculate_volatility(self):
        prices = [1.00, 1.02, 0.98, 1.01]
        volatility = self.vm.calculate_volatility(prices)
        self.assertIsNotNone(volatility)
        self.assertGreaterEqual(volatility, 0)

    def test_adjust_stablecoin_supply(self):
        initial_supply = self.vm.get_stablecoin_supply()
        self.vm.adjust_supply(0.05)  # Example adjustment
        new_supply = self.vm.get_stablecoin_supply()
        self.assertNotEqual(initial_supply, new_supply)

if __name__ == '__main__':
    unittest.main()
