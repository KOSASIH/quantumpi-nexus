import time
from user_authentication import UserAuthentication

def benchmark_authentication():
    auth = UserAuthentication()
    for i in range(1000):
        auth.register(f"user{i}", "password123")
    
    start_time = time.time()
    for i in range(1000):
        auth.login(f"user{i}", "password123")
    end_time = time.time()
    
    print(f"Time taken to authenticate 1000 users: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark_authentication()
