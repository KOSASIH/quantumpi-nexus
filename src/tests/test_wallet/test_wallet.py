# src/tests/test_wallet.py

import unittest
from main.wallet import Wallet, BiometricAuth

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet(user_id="user123")
        self.biometric_auth = BiometricAuth()

    def test_initial_balance(self):
        self.assertEqual(self.wallet.get_balance(), 0.0)

    def test_deposit(self):
        self.wallet.deposit(100)
        self.assertEqual(self.wallet.get_balance(), 100.0)

    def test_withdraw(self):
        self.wallet.deposit(100)
        self.wallet.withdraw(50)
        self.assertEqual(self.wallet.get_balance(), 50.0)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.wallet.withdraw(50)

    def test_transfer(self):
        recipient_wallet = Wallet(user_id="user456")
        self.wallet.deposit(100)
        self.wallet.transfer(recipient_wallet, 50)
        self.assertEqual(self.wallet.get_balance(), 50.0)
        self.assertEqual(recipient_wallet.get_balance(), 50.0)

    def test_biometric_auth(self):
        self.biometric_auth.enroll_user("user123", "biometric_data_123")
        self.assertTrue(self.biometric_auth.authenticate("user123", "biometric_data_123"))
        self.assertFalse(self.biometric_auth.authenticate("user123", "wrong_data"))

if __name__ == '__main__':
    unittest.main()
