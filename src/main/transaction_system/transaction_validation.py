class TransactionValidator:
    def __init__(self, balance_checker):
        self.balance_checker = balance_checker

    def validate(self, transaction):
        if not self.is_valid_amount(transaction.amount):
            return False, "Invalid amount."
        if not self.has_sufficient_balance(transaction.sender, transaction.amount):
            return False, "Insufficient balance."
        return True, "Transaction is valid."

    def is_valid_amount(self, amount):
        return amount > 0

    def has_sufficient_balance(self, sender, amount):
        # Placeholder for balance checking logic
        balance = self.balance_checker.get_balance(sender)
        return balance >= amount

# Example balance checker for demonstration
class BalanceChecker:
    def __init__(self, balances):
        self.balances = balances

    def get_balance(self, account):
        return self.balances.get(account, 0)

# Example usage
if __name__ == "__main__":
    balances = {"Alice": 500, "Bob": 300}
    balance_checker = BalanceChecker(balances)
    validator = TransactionValidator(balance_checker)

    tx = Transaction("Alice", "Bob", 100)
    is_valid, message = validator.validate(tx)
    print("Transaction Valid:", is_valid, "| Message:", message)
