import hashlib
import json
import random
import time
from collections import defaultdict
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Wallet:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0.0
        self.transactions = []
        self.wallet_id = self.generate_wallet_id()
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.transaction_counter = 0

    def generate_wallet_id(self):
        """Generate a unique wallet ID."""
        return hashlib.sha256(f"{self.user_id}{random.randint(1, 100000)}".encode()).hexdigest()

    def deposit(self, amount):
        """Deposit funds into the wallet."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.record_transaction('deposit', amount)
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw funds from the wallet."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.record_transaction('withdraw', amount)
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, recipient_wallet, amount):
        """Transfer funds to another wallet."""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        
        self.withdraw(amount)
        recipient_wallet.deposit(amount)
        self.record_transaction('transfer', amount, recipient_wallet.wallet_id)
        print(f"Transferred {amount} to wallet {recipient_wallet.wallet_id}.")

    def record_transaction(self, transaction_type, amount, recipient_wallet_id=None):
        """Record a transaction with a unique ID and timestamp."""
        transaction_id = self.transaction_counter
        self.transaction_counter += 1
        transaction = {
            'id': transaction_id,
            'type': transaction_type,
            'amount': amount,
            'timestamp': time.time(),
            'recipient_wallet_id': recipient_wallet_id,
            'signature': self.sign_transaction(transaction_id, transaction_type, amount, recipient_wallet_id)
        }
        self.transactions.append(transaction)

    def sign_transaction(self, transaction_id, transaction_type, amount, recipient_wallet_id):
        """Sign a transaction to ensure authenticity."""
        message = f"{transaction_id}:{transaction_type}:{amount}:{recipient_wallet_id}".encode()
        return self.private_key.sign(message).hex()

    def get_balance(self):
        """Get the current balance of the wallet."""
        return self.balance

    def get_transaction_history(self):
        """Get the transaction history of the wallet."""
        return json.dumps(self.transactions, indent=4)

    def verify_transaction(self, transaction):
        """Verify the authenticity of a transaction."""
        message = f"{transaction['id']}:{transaction['type']}:{transaction['amount']}:{transaction['recipient_wallet_id']}".encode()
        signature = bytes.fromhex(transaction['signature'])
        return self.public_key.verify(signature, message)

    def get_wallet_id(self):
        """Get the wallet ID."""
        return self.wallet_id

    def get_public_key(self):
        """Get the public key of the wallet."""
        return self.public_key.to_string().hex()

# Example usage
if __name__ == "__main__":
    wallet1 = Wallet("user1")
    wallet2 = Wallet("user2")
    
    wallet1.deposit(100)
    wallet1.transfer(wallet2, 50)
    print(wallet1.get_transaction_history())
    print(wallet2.get_transaction_history())
