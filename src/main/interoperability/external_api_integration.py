# src/main/interoperability/external_api_integration.py

import requests

class ExternalAPIIntegration:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def fetch_data(self, endpoint):
        """Fetch data from an external API."""
        url = f"{self.api_base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Data fetched successfully from {url}.")
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

    def post_data(self, endpoint, data):
        """Post data to an external API."""
        url = f"{self.api_base_url}/{endpoint}"
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print(f"Data posted successfully to {url}.")
            return response.json()
        else:
            raise Exception(f"Failed to post data to {url}. Status code: {response.status_code}")

    def get_status(self):
        """Check the status of the external API."""
        try:
            response = requests.get(self.api_base_url)
            if response.status_code == 200:
                print("External API is up and running.")
                return True
            else:
                print("External API is down.")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to external API: {e}")
            return False
