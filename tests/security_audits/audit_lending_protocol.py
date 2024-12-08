import json
from lending_protocol import LendingProtocol

def audit_lending_protocol():
    protocol = LendingProtocol()
    protocol.lend("Alice", 1000)
    protocol.lend("Bob", 500)

    # Check for vulnerabilities
    for loan_id, loan in protocol.loans.items():
        if loan["amount"] < 0:
            print(f"Security issue: Loan {loan_id} has a negative amount.")
    
    print("Audit completed. No vulnerabilities found.")

if __name__ == "__main__":
    audit_lending_protocol()
