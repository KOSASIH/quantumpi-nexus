import time
from lending_protocol import LendingProtocol

def benchmark_lending():
    protocol = LendingProtocol()
    start_time = time.time()
    
    for i in range(1000):
        protocol.lend(f"User {i}", 1000)
    
    end_time = time.time()
    print(f"Time taken to lend 1000 loans: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark_lending()
