import unittest
from src.main.governance.proposal_management import ProposalManagement

class TestProposalManagement(unittest.TestCase):

    def setUp(self):
        self.proposal_management = ProposalManagement()

    def test_create_proposal(self):
        proposal_id = self.proposal_management.create_proposal("New feature proposal")
        self.assertEqual(self.proposal_management.get_proposal(proposal_id).description, "New feature proposal")

    def test_update_proposal(self):
        proposal_id = self.proposal_management.create_proposal("Old feature proposal")
        self.proposal_management.update_proposal(proposal_id, "Updated feature proposal")
        self.assertEqual(self.proposal_management.get_proposal(proposal_id).description, "Updated feature proposal")

    def test_delete_proposal(self):
        proposal_id = self.proposal_management.create_proposal("Proposal to delete")
        self.proposal_management.delete_proposal(proposal_id)
        self.assertIsNone(self.proposal_management.get_proposal(proposal_id))

if __name__ == '__main__':
    unittest.main()
