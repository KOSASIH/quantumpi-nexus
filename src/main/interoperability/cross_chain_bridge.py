class CrossChainBridge:
    def __init__(self):
        self.bridges = {}

    def add_bridge(self, chain_name, bridge_address):
        self.bridges[chain_name] = bridge_address

    def transfer(self, from_chain, to_chain, amount, recipient):
        if from_chain not in self.bridges or to_chain not in self.bridges:
            raise Exception("Invalid chain specified.")
        
        # Simulate the transfer process
        print(f"Transferring {amount} from {from_chain} to {to_chain} for recipient {recipient}.")
        # Here you would implement the actual logic for cross-chain transfer
        return True

# Example usage
if __name__ == "__main__":
    bridge = CrossChainBridge()
    bridge.add_bridge("Ethereum", "0xBridgeAddressEthereum")
    bridge.add_bridge("BinanceSmartChain", "0xBridgeAddressBSC")

    try:
        bridge.transfer("Ethereum", "BinanceSmartChain", 100, "0xRecipientAddress")
    except Exception as e:
        print(e)
