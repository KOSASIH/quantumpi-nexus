# src/smart_contracts/pi_stablecoin.py

from web3 import Web3
from eth_account import Account
import json

class PiStablecoin:
    def __init__(self):
        self.name = "Pi Coin"
        self.symbol = "PI"
        self.value = 314.159  # Fixed value in USD
        self.total_supply = 100_000_000_000  # Total supply set to 100 billion
        self.balances = {}
        self.allowances = {}
        self.staking_balances = {}
        self.staking_rewards = {}
        self.proposals = []
        self.votes = {}
        self.owners = []
        self.required_signatures = 2  # For multi-signature wallet
        self.transactions = []
        self.approvals = {}

    def mint(self, amount, to_address):
        """Mint new stablecoins."""
        if self.total_supply + amount > 100_000_000_000:
            raise ValueError("Cannot mint beyond total supply limit of 100,000,000,000.")
        
        if to_address not in self.balances:
            self.balances[to_address] = 0
        self.balances[to_address] += amount
        self.total_supply += amount
        return f"{amount} {self.symbol} minted to {to_address}."

    def transfer(self, to_address, amount):
        """Transfer stablecoins to another address."""
        if self.balances.get(to_address, 0) + amount < 0:
            raise ValueError("Insufficient balance.")
        if self.balances.get(self, 0) < amount:
            raise ValueError("Insufficient balance.")
        
        self.balances[to_address] = self.balances.get(to_address, 0) + amount
        self.balances[self] -= amount
        return f"{amount} {self.symbol} transferred to {to_address}."

    def approve(self, spender, amount):
        """Approve an allowance for another address."""
        if spender not in self.allowances:
            self.allowances[spender] = 0
        self.allowances[spender] += amount
        return f"Approved {amount} {self.symbol} for {spender}."

    def stake(self, amount, staker_address):
        """Stake stablecoins for rewards."""
        if self.balances.get(staker_address, 0) < amount:
            raise ValueError("Insufficient balance to stake.")
        self.balances[staker_address] -= amount
        if staker_address not in self.staking_balances:
            self.staking_balances[staker_address] = 0
        self.staking_balances[staker_address] += amount
        return f"{amount} {self.symbol} staked by {staker_address}."

    def withdraw_stake(self, amount, staker_address):
        """Withdraw staked stablecoins."""
        if self.staking_balances.get(staker_address, 0) < amount:
            raise ValueError("Insufficient staked balance.")
        self.staking_balances[staker_address] -= amount
        self.balances[staker_address] += amount
        return f"{amount} {self.symbol} withdrawn from stake by {staker_address}."

    def create_proposal(self, description):
        """Create a governance proposal."""
        proposal_id = len(self.proposals)
        self.proposals.append({"id": proposal_id, "description": description, "vote_count": 0})
        return f"Proposal created: {description}"

    def vote(self, proposal_id, voter_address):
        """Vote on a governance proposal."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        if voter_address in self.votes.get(proposal_id, []):
            raise ValueError("Already voted on this proposal.")
        if proposal_id not in self.votes:
            self.votes[proposal_id] = []
        self.votes[proposal_id].append(voter_address)
        self.proposals[proposal_id]["vote_count"] += 1
        return f"Voted on proposal {proposal_id} by {voter_address}."

    def add_owner(self, new_owner):
        """Add a new owner for multi-signature wallet."""
        if new_owner not in self.owners:
            self.owners.append(new_owner)
            return f"{new_owner} added as an owner."
        return f"{new_owner} is already an owner."

    def submit_transaction(self, to, value):
        """Submit a transaction for multi-signature approval."""
       
