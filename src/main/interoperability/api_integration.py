import requests

class APIIntegration:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code} - {response.text}")

    def post_data(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Error posting data: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    api = APIIntegration("https://api.example.com")
    try:
        data = api.get_data("financial-data")
        print("Fetched Data:", data)
    except Exception as e:
        print(e)
