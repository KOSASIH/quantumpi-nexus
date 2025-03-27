from web3 import Web3
from eth_account import Account
import json
from collections import defaultdict

class PiStablecoin:
    def __init__(self):
        self.name = "Pi Coin"
        self.symbol = "PI"
        self.value = 314159.00  # Fixed value in USD
        self.total_supply = 100_000_000_000  # Total supply set to 100 billion
        self.balances = defaultdict(int)
        self.allowances = defaultdict(int)
        self.staking_balances = defaultdict(int)
        self.staking_rewards = defaultdict(float)
        self.proposals = []
        self.votes = defaultdict(list)
        self.owners = []
        self.required_signatures = 2  # For multi-signature wallet
        self.transactions = []
        self.approvals = defaultdict(list)

    def mint(self, amount, to_address):
        """Mint new stablecoins."""
        if self.total_supply + amount > 100_000_000_000:
            raise ValueError("Cannot mint beyond total supply limit of 100,000,000,000.")
        
        self.balances[to_address] += amount
        self.total_supply += amount
        self.log_event("Mint", amount, to_address)
        return f"{amount} {self.symbol} minted to {to_address}."

    def transfer(self, to_address, amount):
        """Transfer stablecoins to another address."""
        if self.balances[self] < amount:
            raise ValueError("Insufficient balance.")
        
        self.balances[to_address] += amount
        self.balances[self] -= amount
        self.log_event("Transfer", amount, to_address)
        return f"{amount} {self.symbol} transferred to {to_address}."

    def approve(self, spender, amount):
        """Approve an allowance for another address."""
        self.allowances[spender] += amount
        self.log_event("Approve", amount, spender)
        return f"Approved {amount} {self.symbol} for {spender}."

    def stake(self, amount, staker_address):
        """Stake stablecoins for rewards."""
        if self.balances[staker_address] < amount:
            raise ValueError("Insufficient balance to stake.")
        
        self.balances[staker_address] -= amount
        self.staking_balances[staker_address] += amount
        self.log_event("Stake", amount, staker_address)
        return f"{amount} {self.symbol} staked by {staker_address}."

    def withdraw_stake(self, amount, staker_address):
        """Withdraw staked stablecoins."""
        if self.staking_balances[staker_address] < amount:
            raise ValueError("Insufficient staked balance.")
        
        self.staking_balances[staker_address] -= amount
        self.balances[staker_address] += amount
        self.log_event("Withdraw Stake", amount, staker_address)
        return f"{amount} {self.symbol} withdrawn from stake by {staker_address}."

    def create_proposal(self, description):
        """Create a governance proposal."""
        proposal_id = len(self.proposals)
        self.proposals.append({"id": proposal_id, "description": description, "vote_count": 0})
        self.log_event("Proposal Created", proposal_id, description)
        return f"Proposal created: {description}"

    def vote(self, proposal_id, voter_address):
        """Vote on a governance proposal."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        if voter_address in self.votes[proposal_id]:
            raise ValueError("Already voted on this proposal.")
        
        self.votes[proposal_id].append(voter_address)
        self.proposals[proposal_id]["vote_count"] += 1
        self.log_event("Vote", proposal_id, voter_address)
        return f"Voted on proposal {proposal_id} by {voter_address}."

    def add_owner(self, new_owner):
        """Add a new owner for multi-signature wallet."""
        if new_owner not in self.owners:
            self.owners.append(new_owner)
            self.log_event("Owner Added", new_owner)
            return f"{new_owner} added as an owner."
        return f"{new_owner} is already an owner."

    def submit_transaction(self, to, value):
        """Submit a transaction for multi-signature approval."""
        transaction_id = len(self.transactions)
        self.transactions.append({"to": to, "value": value, "approvals": 0})
        self.log_event("Transaction Submitted", transaction_id, to)
        return f"Transaction submitted to {to} for {value}."

    def approve_transaction(self, transaction_id, owner_address):
        """Approve a submitted transaction."""
        if transaction_id >= len(self.transactions):
            raise ValueError("Invalid transaction ID.")
        if owner_address not in self.owners:
            raise ValueError("Not an owner.")
        if owner_address in self.transactions[transaction_id]["approvals"]:
            raise ValueError("Transaction already approved by this owner.")
        
        self.transactions[transaction_id]["approvals"].append(owner_address)
        self.transactions[transaction_id]["approvals_count"] += 1
        self.log_event("Transaction Approved", transaction_id, owner_address)

        if self.transactions[transaction_id]["approvals_count"] >= self.required_signatures:
            self.execute_transaction(transaction_id)

        return f"Transaction {transaction_id} approved by {owner_address}."

    def execute_transaction(self, transaction_id):
        """Execute a transaction once it has enough approvals."""
        transaction = self.transactions[transaction_id]
        # Logic to transfer funds or execute the transaction
        self.log_event("Transaction Executed", transaction_id, transaction["to"])
        return f"Transaction {transaction_id} executed."

    def log_event(self, event_type, *args):
        """Log events for transparency and auditing."""
        print(f"Event: {event_type}, Details: {args}")

    def get_balance(self, address):
        """Get the balance of an address."""
        return self.balances.get(address, 0)

    def get_staking_balance(self, address):
        """Get the staking balance of an address."""
        return self.staking_balances.get(address, 0)

    def get_proposal(self, proposal_id):
        """Get details of a specific proposal."""
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        return self.proposals[proposal_id]

    def get_transaction(self, transaction_id):
        """Get details of a specific transaction."""
        if transaction_id >= len(self.transactions):
            raise ValueError("Invalid transaction ID.")
        return self.transactions[transaction_id]
