class FiatOnRamp:
    def __init__(self, api_integration):
        self.api_integration = api_integration

    def initiate_purchase(self, fiat_amount, user_wallet):
        # Simulate the process of purchasing stablecoins with fiat
        print(f"Initiating purchase of stablecoins worth {fiat_amount} for wallet {user_wallet}.")
        # Here you would implement the actual logic for fiat conversion
        return True

    def get_exchange_rate(self, fiat_currency):
        # Fetch the current exchange rate for the specified fiat currency
        try:
            rate_data = self.api_integration.get_data(f"exchange-rate/{fiat_currency}")
            return rate_data['rate']
        except Exception as e:
            print(e)
            return None

# Example usage
if __name__ == "__main__":
    api = APIIntegration("https://api.example.com")
    fiat_on_ramp = FiatOnRamp(api)

    try:
        exchange_rate = fiat_on_ramp.get_exchange_rate("USD")
        print("Current Exchange Rate (USD to Stablecoin):", exchange_rate)

        fiat_on_ramp.initiate_purchase(100, "0xUser WalletAddress")
    except Exception as e:
        print(e)
