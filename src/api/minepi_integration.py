# src/api/minepi_integration.py

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base URL for the minepi.com API (this is a placeholder; replace with the actual API endpoint)
MINEPI_API_URL = "https://api.minepi.com"  # Example URL; adjust as necessary

def get_minepi_balance(user_id):
    """Fetch user balance from minepi.com."""
    try:
        response = requests.get(f"{MINEPI_API_URL}/user/{user_id}/balance")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/api/minepi/balance', methods=['GET'])
def minepi_balance():
    """API endpoint to get the balance of a user from minepi.com."""
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400
    
    balance_data = get_minepi_balance(user_id)
    
    if "error" in balance_data:
        return jsonify(balance_data), 500  # Internal server error if API call fails
    
    return jsonify(balance_data)

if __name__ == "__main__":
    app.run(debug=True)
