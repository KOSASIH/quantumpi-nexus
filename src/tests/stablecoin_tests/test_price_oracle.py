import unittest
from src.main.stablecoin.price_oracle import PriceOracle

class TestPriceOracle(unittest.TestCase):

    def setUp(self):
        self.oracle = PriceOracle()

    def test_get_current_price(self):
        price = self.oracle.get_current_price("USD")
        self.assertIsNotNone(price)
        self.assertGreater(price, 0)

    def test_price_update(self):
        initial_price = self.oracle.get_current_price("USD")
        self.oracle.update_price("USD", 1.05)
        updated_price = self.oracle.get_current_price("USD")
        self.assertNotEqual(initial_price, updated_price)

if __name__ == '__main__':
    unittest.main()
