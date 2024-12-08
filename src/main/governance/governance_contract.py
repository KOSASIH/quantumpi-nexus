class GovernanceContract:
    def __init__(self):
        self.proposals = {}
        self.votes = {}
        self.proposal_count = 0

    def create_proposal(self, description):
        self.proposal_count += 1
        proposal_id = self.proposal_count
        self.proposals[proposal_id] = {
            "description": description,
            "votes_for": 0,
            "votes_against": 0,
            "status": "Pending"
        }
        return proposal_id

    def vote(self, proposal_id, voter, vote_type):
        if proposal_id not in self.proposals:
            return "Proposal does not exist."
        
        if voter in self.votes.get(proposal_id, []):
            return "Voter has already voted on this proposal."

        if vote_type == "for":
            self.proposals[proposal_id]["votes_for"] += 1
        elif vote_type == "against":
            self.proposals[proposal_id]["votes_against"] += 1
        else:
            return "Invalid vote type."

        self.votes.setdefault(proposal_id, []).append(voter)
        return "Vote recorded."

    def finalize_proposal(self, proposal_id):
        if proposal_id not in self.proposals:
            return "Proposal does not exist."
        
        proposal = self.proposals[proposal_id]
        if proposal["votes_for"] > proposal["votes_against"]:
            proposal["status"] = "Approved"
        else:
            proposal["status"] = "Rejected"
        return proposal

# Example usage
if __name__ == "__main__":
    governance = GovernanceContract()
    proposal_id = governance.create_proposal("Increase transaction fee by 0.01")
    print("Proposal ID:", proposal_id)

    governance.vote(proposal_id, "Alice", "for")
    governance.vote(proposal_id, "Bob", "against")
    result = governance.finalize_proposal(proposal_id)
    print("Final Proposal Status:", result)
