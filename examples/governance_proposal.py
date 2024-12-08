# governance_proposal.py - Example of a governance proposal

import json
import uuid
from datetime import datetime

class GovernanceProposal:
    def __init__(self, proposer, description):
        self.proposal_id = str(uuid.uuid4())
        self.proposer = proposer
        self.description = description
        self.timestamp = datetime.now().isoformat()
        self.votes = {"for": 0, "against": 0}

    def vote(self, vote_type):
        if vote_type in self.votes:
            self.votes[vote_type] += 1
        else:
            raise ValueError("Vote type must be 'for' or 'against'.")

    def to_dict(self):
        return {
            "proposal_id": self.proposal_id,
            "proposer": self.proposer,
            "description": self.description,
            "timestamp": self.timestamp,
            "votes": self.votes
        }

# Example usage
if __name__ == "__main__":
    proposal = GovernanceProposal("Alice", "Increase block size limit.")
    proposal.vote("for")
    proposal.vote("against")
    print(json.dumps(proposal.to_dict(), indent=4))
