# transaction_tests/test_validation.py

import unittest
from transaction_validator import TransactionValidator

class TestTransactionValidator(unittest.TestCase):

    def setUp(self):
        self.validator = TransactionValidator()

    def test_validate_transaction_format(self):
        transaction = {'amount': 100, 'currency': 'USD', 'recipient': 'user123'}
        self.assertTrue(self.validator.validate_format(transaction))

    def test_validate_transaction_amount(self):
        transaction = {'amount': 100, 'currency': 'USD', 'recipient': 'user123'}
        self.assertTrue(self.validator.validate_amount(transaction['amount']))

        transaction_invalid = {'amount': -50, 'currency': 'USD', 'recipient': 'user123'}
        self.assertFalse(self.validator.validate_amount(transaction_invalid['amount']))

if __name__ == '__main__':
    unittest.main()
