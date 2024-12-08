import unittest
from src.main.governance.governance_contract import GovernanceContract

class TestGovernanceContract(unittest.TestCase):

    def setUp(self):
        self.contract = GovernanceContract()

    def test_initial_state(self):
        self.assertEqual(self.contract.get_proposals_count(), 0)
        self.assertEqual(self.contract.get_active_proposals(), [])

    def test_add_proposal(self):
        proposal_id = self.contract.add_proposal("Increase block size")
        self.assertEqual(self.contract.get_proposal(proposal_id).description, "Increase block size")
        self.assertEqual(self.contract.get_proposals_count(), 1)

    def test_proposal_voting(self):
        proposal_id = self.contract.add_proposal("Increase block size")
        self.contract.vote(proposal_id, "yes")
        self.assertEqual(self.contract.get_proposal(proposal_id).votes_yes, 1)
        self.assertEqual(self.contract.get_proposal(proposal_id).votes_no, 0)

if __name__ == '__main__':
    unittest.main()
