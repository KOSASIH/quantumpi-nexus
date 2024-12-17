# src/main/interoperability/cross_chain_protocol.py

class CrossChainProtocol:
    def __init__(self):
        self.chains = {}

    def register_chain(self, chain_id, chain_info):
        """Register a new blockchain in the protocol."""
        if chain_id not in self.chains:
            self.chains[chain_id] = chain_info
            print(f"Chain {chain_id} registered successfully.")
        else:
            print(f"Chain {chain_id} is already registered.")

    def transfer_asset(self, from_chain_id, to_chain_id, asset, amount):
        """Transfer an asset from one chain to another."""
        if from_chain_id not in self.chains or to_chain_id not in self.chains:
            raise ValueError("Both chains must be registered.")

        # Placeholder for actual transfer logic
        print(f"Transferring {amount} of {asset} from {from_chain_id} to {to_chain_id}.")
        # Here you would implement the logic to lock the asset on the source chain
        # and mint or release it on the destination chain.

    def get_chain_info(self, chain_id):
        """Retrieve information about a registered chain."""
        return self.chains.get(chain_id, None)

    def list_chains(self):
        """List all registered chains."""
        return self.chains.keys()
