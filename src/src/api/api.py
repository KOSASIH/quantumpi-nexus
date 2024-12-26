# src/api/api.py

from flask import Flask, request, jsonify
from smart_contracts.pi_stablecoin import PiStablecoin
from governance.governance import Governance

app = Flask(__name__)

# Initialize the stablecoin and governance instances
stablecoin = PiStablecoin(initial_supply=10000)
governance = Governance()

@app.route('/api/stablecoin/mint', methods=['POST'])
def mint_stablecoin():
    """Mint new stablecoins."""
    data = request.json
    amount = data.get('amount')
    to_address = data.get('to_address')
    
    if not amount or not to_address:
        return jsonify({"error": "Amount and to_address are required."}), 400
    
    result = stablecoin.mint(amount, to_address)
    return jsonify({"message": result})

@app.route('/api/stablecoin/transfer', methods=['POST'])
def transfer_stablecoin():
    """Transfer stablecoins to another address."""
    data = request.json
    to_address = data.get('to_address')
    amount = data.get('amount')
    
    if not to_address or not amount:
        return jsonify({"error": "To_address and amount are required."}), 400
    
    try:
        result = stablecoin.transfer(to_address, amount)
        return jsonify({"message": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stablecoin/stake', methods=['POST'])
def stake_stablecoin():
    """Stake stablecoins for rewards."""
    data = request.json
    amount = data.get('amount')
    staker_address = data.get('staker_address')
    
    if not amount or not staker_address:
        return jsonify({"error": "Amount and staker_address are required."}), 400
    
    try:
        result = stablecoin.stake(amount, staker_address)
        return jsonify({"message": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/governance/proposal', methods=['POST'])
def create_proposal():
    """Create a new governance proposal."""
    data = request.json
    description = data.get('description')
    proposer_address = data.get('proposer_address')
    
    if not description or not proposer_address:
        return jsonify({"error": "Description and proposer_address are required."}), 400
    
    try:
        result = governance.create_proposal(description, proposer_address)
        return jsonify({"message": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/governance/vote', methods=['POST'])
def vote_proposal():
    """Vote on a governance proposal."""
    data = request.json
    proposal_id = data.get('proposal_id')
    voter_address = data.get('voter_address')
    
    if not proposal_id or not voter_address:
        return jsonify({"error": "Proposal ID and voter_address are required."}), 400
    
    try:
        result = governance.vote(proposal_id, voter_address)
        return jsonify({"message": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/governance/execute', methods=['POST'])
def execute_proposal():
    """Execute a governance proposal."""
    data = request.json
    proposal_id = data.get('proposal_id')
    
    if not proposal_id:
        return jsonify({"error": "Proposal ID is required."}), 400
    
    try:
        result = governance.execute_proposal(proposal_id)
        return jsonify({"message": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/minepi/balance', methods=['GET'])
def get_minepi_balance():
    """Fetch user balance from minepi.com."""
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({"error": "User  ID is required."}), 400
    
    # Simulated response for integration with minepi.com
    balance = stablecoin.integrate_with_minepi(user_id)
    return jsonify({"balance": balance})

@app.route('/api/stablecoin/balance', methods=['GET'])
def get_balance():
    """Get the balance of a specific address."""
    address = request.args.get('address')
    
    if not address:
        return jsonify({"error": "Address is required."}), 400
    
    balance = stablecoin.get_balance(address
    return jsonify({"balance": balance})

@app.route('/api/stablecoin/staking_balance', methods=['GET'])
def get_staking_balance():
    """Get the staking balance of a specific address."""
    address = request.args.get('address')
    
    if not address:
        return jsonify({"error": "Address is required."}), 400
    
    staking_balance = stablecoin.get_staking_balance(address)
    return jsonify({"staking_balance": staking_balance})

@app.route('/api/governance/proposals', methods=['GET'])
def list_proposals():
    """Get all governance proposals."""
    proposals = governance.get_proposals()
    return jsonify({"proposals": proposals})

@app.route('/api/governance/votes', methods=['GET'])
def get_votes():
    """Get votes for a specific proposal."""
    proposal_id = request.args.get('proposal_id')
    
    if not proposal_id:
        return jsonify({"error": "Proposal ID is required."}), 400
    
    try:
        votes = governance.get_votes(int(proposal_id))
        return jsonify({"votes": votes})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
