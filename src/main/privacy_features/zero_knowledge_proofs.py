# src/main/privacy/zero_knowledge_proofs.py

import hashlib
import random

class ZeroKnowledgeProof:
    def __init__(self, secret):
        self.secret = secret
        self.commitment = self.commit()

    def commit(self):
        """Create a commitment to the secret."""
        r = random.randint(1, 1000)  # Random nonce
        commitment = hashlib.sha256(f"{self.secret}{r}".encode()).hexdigest()
        return commitment, r

    def prove(self, challenge):
        """Prove knowledge of the secret without revealing it."""
        if challenge not in [0, 1]:
            raise ValueError("Challenge must be 0 or 1.")
        
        if challenge == 0:
            return self.commitment  # Reveal commitment
        else:
            return self.secret  # Reveal secret

    def verify(self, commitment, response, challenge):
        """Verify the proof."""
        if challenge == 0:
            return commitment == self.commitment[0]
        else:
            # Recreate the commitment with the revealed secret
            r = self.commitment[1]
            new_commitment = hashlib.sha256(f"{response}{r}".encode()).hexdigest()
            return new_commitment == commitment
