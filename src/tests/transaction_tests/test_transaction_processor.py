# transaction_tests/test_transaction_processor.py

import unittest
from transaction_processor import TransactionProcessor

class TestTransactionProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = TransactionProcessor()

    def test_process_valid_transaction(self):
        transaction = {'amount': 100, 'currency': 'USD', 'recipient': 'user123'}
        result = self.processor.process(transaction)
        self.assertTrue(result['success'])
        self.assertEqual(result['status'], 'processed')

    def test_process_invalid_transaction(self):
        transaction = {'amount': -50, 'currency': 'USD', 'recipient': 'user123'}
        result = self.processor.process(transaction)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], 'Invalid transaction')

if __name__ == '__main__':
    unittest.main()
