class VotingMechanism:
    def __init__(self, governance_contract):
        self.governance_contract = governance_contract

    def cast_vote(self, proposal_id, voter, vote_type):
        return self.governance_contract.vote(proposal_id, voter, vote_type)

    def get_results(self, proposal_id):
        if proposal_id not in self.governance_contract.proposals:
            return "Proposal does not exist."
        
        proposal = self.governance_contract.proposals[proposal_id]
        return {
            "votes_for": proposal["votes_for"],
            "votes_against": proposal["votes_against"],
            "status": proposal["status"]
        }

# Example usage
if __name__ == "__main__":
    governance = GovernanceContract()
    voting = VotingMechanism(governance)

    proposal_id = governance.create_proposal("Increase transaction fee by 0.01")
    voting.cast_vote(proposal_id, "Alice", "for")
    voting.cast_vote(proposal_id, "Bob", "against")

    results = voting.get_results(proposal_id)
    print("Voting Results:", results)
