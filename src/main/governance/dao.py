# src/main/governance/dao.py

class DAO:
    def __init__(self):
        self.members = {}
        self.proposals = {}
        self.proposal_count = 0

    def add_member(self, member_id):
        """Add a new member to the DAO."""
        if member_id not in self.members:
            self.members[member_id] = {'votes': 0, 'proposals': []}
            print(f"Member {member_id} added to the DAO.")
        else:
            print(f"Member {member_id} already exists.")

    def create_proposal(self, proposal_description, proposer_id):
        """Create a new proposal."""
        if proposer_id not in self.members:
            raise ValueError("Proposer is not a member of the DAO.")
        
        self.proposal_count += 1
        proposal_id = self.proposal_count
        self.proposals[proposal_id] = {
            'description': proposal_description,
            'votes': 0,
            'proposer': proposer_id,
            'status': 'pending'
        }
        self.members[proposer_id]['proposals'].append(proposal_id)
        print(f"Proposal {proposal_id} created by {proposer_id}: {proposal_description}")
        return proposal_id

    def get_proposal(self, proposal_id):
        """Retrieve a proposal by its ID."""
        return self.proposals.get(proposal_id, None)

    def get_all_proposals(self):
        """Retrieve all proposals."""
        return self.proposals

    def vote(self, proposal_id, member_id):
        """Vote on a proposal."""
        if member_id not in self.members:
            raise ValueError("Member is not part of the DAO.")
        
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        if proposal['status'] != 'pending':
            raise ValueError("Voting is closed for this proposal.")
        
        proposal['votes'] += 1
        self.members[member_id]['votes'] += 1
        print(f"Member {member_id} voted on proposal {proposal_id}. Total votes: {proposal['votes']}")

    def finalize_proposal(self, proposal_id):
        """Finalize a proposal based on the votes."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        if proposal['status'] == 'pending':
            proposal['status'] = 'finalized'
            print(f"Proposal {proposal_id} has been finalized with {proposal['votes']} votes.")
        else:
            print(f"Proposal {proposal_id} is already finalized.")
