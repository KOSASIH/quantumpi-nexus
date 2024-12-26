# src/governance/governance.py

class Governance:
    def __init__(self):
        self.proposals = []
        self.votes = {}
        self.quorum = 0.5  # Minimum percentage of votes required to pass a proposal
        self.owners = []  # List of addresses that can create proposals

    def add_owner(self, owner_address):
        """Add a new owner who can create proposals."""
        if owner_address not in self.owners:
            self.owners.append(owner_address)
            return f"{owner_address} added as a governance owner."
        return f"{owner_address} is already an owner."

    def create_proposal(self, description, proposer_address):
        """Create a new governance proposal."""
        if proposer_address not in self.owners:
            raise ValueError("Only owners can create proposals.")
        proposal_id = len(self.proposals)
        self.proposals.append({
            "id": proposal_id,
            "description": description,
            "vote_count": 0,
            "voters": set(),
            "executed": False
        })
        return f"Proposal created: {description} (ID: {proposal_id})"

    def vote(self, proposal_id, voter_address):
        """Vote on a governance proposal."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        if voter_address in self.proposals[proposal_id]["voters"]:
            raise ValueError("Already voted on this proposal.")
        
        self.proposals[proposal_id]["vote_count"] += 1
        self.proposals[proposal_id]["voters"].add(voter_address)
        return f"Voted on proposal {proposal_id} by {voter_address}."

    def execute_proposal(self, proposal_id):
        """Execute a proposal if it has enough votes."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        proposal = self.proposals[proposal_id]

        if proposal["executed"]:
            raise ValueError("Proposal has already been executed.")
        
        total_votes = proposal["vote_count"]
        if total_votes / len(self.owners) >= self.quorum:
            # Logic to execute the proposal (this could be a function call or state change)
            proposal["executed"] = True
            return f"Proposal {proposal_id} executed: {proposal['description']}"
        else:
            raise ValueError("Not enough votes to execute the proposal.")

    def get_proposals(self):
        """Get all proposals."""
        return self.proposals

    def get_votes(self, proposal_id):
        """Get the list of voters for a specific proposal."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        return list(self.proposals[proposal_id]["voters"])

# Example usage
if __name__ == "__main__":
    governance = Governance()
    governance.add_owner("0x123")
    governance.add_owner("0x456")
    print(governance.create_proposal("Increase supply by 1000", "0x123"))
    print(governance.vote(0, "0x123"))
    print(governance.vote(0, "0x456"))
    print(governance.execute_proposal(0))
    print(governance.get_proposals())
