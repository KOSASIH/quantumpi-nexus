# lending_example.py - Example of using the lending protocol

class LendingProtocol:
    def __init__(self):
        self.loans = {}  # Dictionary to store loans
        self.loan_id_counter = 1  # Counter for unique loan IDs

    def lend(self, borrower, amount):
        """Lend a specified amount to a borrower."""
        loan_id = self.loan_id_counter
        self.loans[loan_id] = {
            "borrower": borrower,
            "amount": amount,
            "repaid": False
        }
        self.loan_id_counter += 1
        return loan_id

    def repay(self, loan_id):
        """Repay a loan by its ID."""
        if loan_id in self.loans:
            if not self.loans[loan_id]["repaid"]:
                self.loans[loan_id]["repaid"] = True
                return f"Loan {loan_id} repaid successfully."
            else:
                return f"Loan {loan_id} has already been repaid."
        else:
            return "Loan ID not found."

    def check_loan_status(self, loan_id):
        """Check the status of a loan."""
        if loan_id in self.loans:
            loan = self.loans[loan_id]
            status = "Repaid" if loan["repaid"] else "Outstanding"
            return {
                "loan_id": loan_id,
                "borrower": loan["borrower"],
                "amount": loan["amount"],
                "status": status
            }
        else:
            return "Loan ID not found."

# Example usage
if __name__ == "__main__":
    lending_protocol = LendingProtocol()

    # Lend money to borrowers
    loan1 = lending_protocol.lend("Alice", 1000)
    loan2 = lending_protocol.lend("Bob", 500)

    print(f"Loan ID {loan1} lent to Alice for $1000.")
    print(f"Loan ID {loan2} lent to Bob for $500.")

    # Check loan status
    print(lending_protocol.check_loan_status(loan1))
    print(lending_protocol.check_loan_status(loan2))

    # Repay a loan
    print(lending_protocol.repay(loan1))

    # Check loan status again
    print(lending_protocol.check_loan_status(loan1))
    print(lending_protocol.check_loan_status(loan2))
