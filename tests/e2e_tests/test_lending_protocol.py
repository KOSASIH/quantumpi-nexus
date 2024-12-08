import unittest
from lending_protocol import LendingProtocol

class TestLendingProtocol(unittest.TestCase):
    def setUp(self):
        self.protocol = LendingProtocol()

    def test_lending_and_repayment(self):
        loan_id = self.protocol.lend("Alice", 1000)
        self.assertEqual(self.protocol.check_loan_status(loan_id)["status"], "Outstanding")
        
        repayment_message = self.protocol.repay(loan_id)
        self.assertIn("repaid successfully", repayment_message)
        self.assertEqual(self.protocol.check_loan_status(loan_id)["status"], "Repaid")

    def test_invalid_loan_repayment(self):
        response = self.protocol.repay(999)  # Invalid loan ID
        self.assertEqual(response, "Loan ID not found.")

if __name__ == "__main__":
    unittest.main()
