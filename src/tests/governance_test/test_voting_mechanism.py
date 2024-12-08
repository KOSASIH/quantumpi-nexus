import unittest
from src.main.governance.voting_mechanism import VotingMechanism

class TestVotingMechanism(unittest.TestCase):

    def setUp(self):
        self.voting_mechanism = VotingMechanism()

    def test_vote_casting(self):
        self.voting_mechanism.cast_vote("user1", "proposal1", "yes")
        self.assertIn("user1", self.voting_mechanism.get_votes("proposal1")["yes"])

    def test_vote_count(self):
        self.voting_mechanism.cast_vote("user1", "proposal1", "yes")
        self.voting_mechanism.cast_vote("user2", "proposal1", "no")
        self.assertEqual(self.voting_mechanism.get_vote_count("proposal1"), {"yes": 1, "no": 1})

    def test_invalid_vote(self):
        with self.assertRaises(ValueError):
            self.voting_mechanism.cast_vote("user1", "proposal1", "maybe")

if __name__ == '__main__':
    unittest.main()
