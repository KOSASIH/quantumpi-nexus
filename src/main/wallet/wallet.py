# src/main/wallet/wallet.py

import hashlib
import json
import random

class Wallet:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0.0
        self.transactions = []
        self.wallet_id = self.generate_wallet_id()

    def generate_wallet_id(self):
        """Generate a unique wallet ID."""
        return hashlib.sha256(f"{self.user_id}{random.randint(1, 100000)}".encode()).hexdigest()

    def deposit(self, amount):
        """Deposit funds into the wallet."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw funds from the wallet."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append({'type': 'withdraw', 'amount': amount})
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        """Get the current balance of the wallet."""
        return self.balance

    def get_transaction_history(self):
        """Get the transaction history of the wallet."""
        return json.dumps(self.transactions, indent=4)

    def transfer(self, recipient_wallet, amount):
        """Transfer funds to another wallet."""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        
        self.withdraw(amount)
        recipient_wallet.deposit(amount)
        print(f"Transferred {amount} to wallet {recipient_wallet.wallet_id}.")
