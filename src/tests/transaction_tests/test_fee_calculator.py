import unittest
from fee_calculator import FeeCalculator

class TestFeeCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = FeeCalculator()

    def test_fee_calculation_standard(self):
        transaction_amount = 1000
        expected_fee = 10  # Assuming a fee of 1%
        self.assertEqual(self.calculator.calculate_fee(transaction_amount), expected_fee)

    def test_fee_calculation_high_amount(self):
        transaction_amount = 100000
        expected_fee = 1000  # 1% fee
        self.assertEqual(self.calculator.calculate_fee(transaction_amount), expected_fee)

    def test_fee_calculation_low_amount(self):
        transaction_amount = 50
        expected_fee = 0.5  # 1% fee
        self.assertEqual(self.calculator.calculate_fee(transaction_amount), expected_fee)

    def test_fee_calculation_zero_amount(self):
        transaction_amount = 0
        expected_fee = 0  # No fee for zero amount
        self.assertEqual(self.calculator.calculate_fee(transaction_amount), expected_fee)

    def test_fee_calculation_negative_amount(self):
        transaction_amount = -100
        expected_fee = 0  # Assuming no fee for negative amounts
        self.assertEqual(self.calculator.calculate_fee(transaction_amount), expected_fee)

if __name__ == '__main__':
    unittest.main()
