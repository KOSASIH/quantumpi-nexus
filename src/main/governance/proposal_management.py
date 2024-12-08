class ProposalManagement:
    def __init__(self, governance_contract):
        self.governance_contract = governance_contract

    def create_proposal(self, description):
        return self.governance_contract.create_proposal(description)

    def vote_on_proposal(self, proposal_id, voter, vote_type):
        return self.governance_contract.vote(proposal_id, voter, vote_type)

    def finalize_proposal(self, proposal_id):
        return self.governance_contract.finalize_proposal(proposal_id)

# Example usage
if __name__ == "__main__":
    governance = GovernanceContract()
    proposal_manager = ProposalManagement(governance)

    proposal_id = proposal_manager.create_proposal("Increase transaction fee by 0.01")
    print("Proposal ID:", proposal_id)

    proposal_manager.vote_on_proposal(proposal_id, "Alice", "for")
    proposal_manager.vote_on_proposal(proposal_id, "Bob", "against")
    final_status = proposal_manager.finalize_proposal(proposal_id)
    print("Final Proposal Status:", final_status)
