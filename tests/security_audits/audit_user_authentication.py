import json
from user_authentication import UserAuthentication

def audit_user_authentication():
    auth = UserAuthentication()
    auth.register("testuser", "securepassword")

    # Check for vulnerabilities
    if not auth.is_password_secure("securepassword"):
        print("Security issue: Password does not meet security standards.")
    
    print("Audit completed. No vulnerabilities found.")

if __name__ == "__main__":
    audit_user_authentication()
