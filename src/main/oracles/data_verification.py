import hashlib
import json
import requests

class DataVerification:
    def __init__(self, verification_service_url=None):
        """
        Initialize the DataVerification class.

        :param verification_service_url: Optional URL of an external verification service.
        """
        self.verification_service_url = verification_service_url

    def generate_hash(self, data):
        """
        Generate a SHA-256 hash for the given data.

        :param data: The data to hash (should be a dictionary).
        :return: The SHA-256 hash of the data.
        """
        data_string = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(data_string).hexdigest()

    def verify_data(self, data, expected_hash):
        """
        Verify the integrity of the data by comparing its hash with the expected hash.

        :param data: The data to verify (should be a dictionary).
        :param expected_hash: The expected hash to compare against.
        :return: True if the data is valid, False otherwise.
        """
        calculated_hash = self.generate_hash(data)
        return calculated_hash == expected_hash

    def verify_with_service(self, data, expected_hash):
        """
        Verify the data with an external verification service.

        :param data: The data to verify (should be a dictionary).
        :param expected_hash: The expected hash to compare against.
        :return: True if the data is valid according to the service, False otherwise.
        """
        if not self.verification_service_url:
            raise ValueError("No verification service URL provided.")

        verification_payload = {
            'data': data,
            'expected_hash': expected_hash
        }
        try:
            response = requests.post(self.verification_service_url, json=verification_payload)
            response.raise_for_status()
            return response.json().get('is_valid', False)
        except requests.RequestException as e:
            print(f"Error verifying data with service: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize the verifier with an optional external service URL
    verifier = DataVerification('https://verification.service/api/verify')

    # Sample data
    data = {'price': 100, 'timestamp': '2023-10-01T12:00:00Z'}
    
    # Generate hash for the data
    expected_hash = verifier.generate_hash(data)
    print(f"Expected Hash: {expected_hash}")

    # Verify data locally
    is_valid = verifier.verify_data(data, expected_hash)
    print(f"Data valid (local verification): {is_valid}")

    # Verify data with external service
    is_valid_service = verifier.verify_with_service(data, expected_hash)
    print(f"Data valid (external service verification): {is_valid_service}")
