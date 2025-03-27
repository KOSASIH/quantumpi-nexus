// tests/unit_tests.py

import unittest
from smart_contracts.pi_stablecoin import PiStablecoin
from governance.governance import Governance
from api.api import app  # Import the Flask app for API testing

class TestPiStablecoin(unittest.TestCase):
    def setUp(self):
        self.stablecoin = PiStablecoin(initial_supply=10000)

    def test_mint(self):
        result = self.stablecoin.mint(500, "0x123")
        self.assertEqual(self.stablecoin.balances["0x123"], 500)
        self.assertEqual(self.stablecoin.total_supply, 10500)

    def test_transfer(self):
        self.stablecoin.mint(500, "0x123")
        result = self.stablecoin.transfer("0x456", 200)
        self.assertEqual(self.stablecoin.balances["0x123"], 300)
        self.assertEqual(self.stablecoin.balances.get("0x456", 0), 200)

    def test_transfer_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.stablecoin.transfer("0x456", 200)

    def test_stake(self):
        self.stablecoin.mint(500, "0x123")
        result = self.stablecoin.stake(300, "0x123")
        self.assertEqual(self.stablecoin.staking_balances["0x123"], 300)
        self.assertEqual(self.stablecoin.balances["0x123"], 200)

    def test_withdraw_stake(self):
        self.stablecoin.mint(500, "0x123")
        self.stablecoin.stake(300, "0x123")
        result = self.stablecoin.withdraw_stake(100, "0x123")
        self.assertEqual(self.stablecoin.staking_balances["0x123"], 200)
        self.assertEqual(self.stablecoin.balances["0x123"], 300)

    def test_create_proposal(self):
        governance = Governance()
        governance.add_owner("0x123")
        result = governance.create_proposal("Increase supply by 1000", "0x123")
        self.assertEqual(len(governance.proposals), 1)
        self.assertEqual(governance.proposals[0]["description"], "Increase supply by 1000")

    def test_vote(self):
        governance = Governance()
        governance.add_owner("0x123")
        governance.create_proposal("Increase supply by 1000", "0x123")
        result = governance.vote(0, "0x123")
        self.assertEqual(governance.proposals[0]["vote_count"], 1)

    def test_execute_proposal(self):
        governance = Governance()
        governance.add_owner("0x123")
        governance.add_owner("0x456")
        governance.create_proposal("Increase supply by 1000", "0x123")
        governance.vote(0, "0x123")
        governance.vote(0, "0x456")
        result = governance.execute_proposal(0)
        self.assertTrue(governance.proposals[0]["executed"])

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_mint_api(self):
        response = self.app.post('/api/stablecoin/mint', json={'amount': 500, 'to_address': '0x123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_transfer_api(self):
        self.app.post('/api/stablecoin/mint', json={'amount': 500, 'to_address': '0x123'})
        response = self.app.post('/api/stablecoin/transfer', json={'to_address': '0x456', 'amount': 200})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_transfer_insufficient_balance_api(self):
        response = self.app.post('/api/stablecoin/transfer', json={'to_address': '0x456', 'amount': 200})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_create_proposal_api(self):
        response = self.app.post('/api/governance/proposal', json={'description': 'Increase supply by 1000', 'proposer_address': '0x123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_vote_api(self):
        # First, create a proposal
        self.app.post('/api/governance/proposal', json={'description': 'Increase supply by 1000', 'proposer_address': '0x123'})
        response = self.app.post('/api/governance/vote', json={'proposal_id': 0, 'voter_address': '0x123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_execute_proposal_api(self):
        # Create a proposal and vote on it
        self.app.post('/api/governance/proposal', json={'description': 'Increase supply by 1000', 'proposer_address': '0x123'})
        self.app.post('/api/governance/vote', json={'proposal_id': 0, 'voter_address': '0x123'})
        self.app.post('/api/governance/vote', json={'proposal_id': 0, 'voter_address': '0x456'})
        response = self.app.post('/api/governance/execute', json={'proposal_id': 0})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_get_balance_api(self):
        self.app.post('/api/stablecoin/mint', json={'amount': 500, 'to_address': '0x123'})
        response = self.app.get('/api/stablecoin/balance?address=0x123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['balance'], 500)

    def test_get_staking_balance_api(self):
        self.app.post('/api/stablecoin/mint', json={'amount': 500, 'to_address': '0x123'})
        self.app.post('/api/stablecoin/stake', json={'amount': 300, 'staker_address': '0x123'})
        response = self.app.get('/api/stablecoin/staking_balance?address=0x123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['staking_balance'], 300)

    def test_list_proposals_api(self):
        self.app.post('/api/governance/proposal', json={'description': 'Increase supply by 1000', 'proposer_address': '0x123'})
        response = self.app.get('/api/governance/proposals')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()['proposals']), 1)

    def test_get_votes_api(self):
        self.app.post('/api/governance/proposal', json={'description': 'Increase supply by 1000', 'proposer_address': '0x123'})
        self.app.post('/api/governance/vote', json={'proposal_id': 0, 'voter_address': '0x123'})
        response = self.app.get('/api/governance/votes?proposal_id=0')
        self.assertEqual(response.status_code, 200)
        self.assertIn('votes', response.get_json())

if __name__ == "__main__":
    unittest.main()
