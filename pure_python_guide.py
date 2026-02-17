"""
Guide: Pure Python Implementation (Manual Boilerplate)
This script demonstrates the traditional way of creating data containers
in Python, involving manual implementation of methods like __init__, 
__repr__, and __eq__ to match the functionality of dataclasses.
"""

from typing import List, Optional
from datetime import datetime

class User:
    """Manual implementation of a data container."""
    def __init__(self, id: int, username: str, email: str, is_active: bool = True, tags: List[str] = None):
        # We must manually assign every argument to self
        self._id = id
        self._username = username
        self._email = email
        self._is_active = is_active
        # Mutable default protection (standard Python pattern)
        self._tags = tags if tags is not None else []
        
        # Validation
        if "@" not in self._email:
             print(f"Warning: Invalid email format for {self._username}")

    # To mimic frozen=True, we use properties without setters
    @property
    def id(self): return self._id
    
    @property
    def username(self): return self._username
    
    @property
    def email(self): return self._email
    
    @property
    def is_active(self): return self._is_active
    
    @property
    def tags(self): return self._tags

    # Manual __repr__ for readable output
    def __repr__(self):
        return (f"User(id={self.id}, username='{self.username}', "
                f"email='{self.email}', is_active={self.is_active}, tags={self.tags})")

    # Manual __eq__ for value-based comparison
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return (self.id == other.id and 
                self.username == other.username and 
                self.email == other.email and 
                self.is_active == other.is_active and 
                self.tags == other.tags)

class Transaction:
    """A standard class representing a financial transaction."""
    def __init__(self, amount: float, description: str, timestamp: datetime = None):
        self.amount = amount
        self.description = description
        self.timestamp = timestamp if timestamp is not None else datetime.now()

    def display_amount(self):
        return f"${self.amount:,.2f}"

    def __repr__(self):
        return f"Transaction(amount={self.amount}, description='{self.description}', timestamp={self.timestamp})"

if __name__ == "__main__":
    print("--- 1. Standard Class Usage (Manual) ---")
    u1 = User(id=1, username="arthur", email="arthur@example.com", tags=["python", "dev"])
    u2 = User(id=1, username="arthur", email="arthur@example.com", tags=["python", "dev"])
    
    # Needs manual __repr__ to look like this
    print(f"User 1: {u1}")
    
    # Needs manual __eq__ or this would be False (compares memory address otherwise)
    print(f"u1 == u2: {u1 == u2}") 

    print("\n--- 2. Manual Immutability (Read-only properties) ---")
    try:
        u1.username = "modified"
    except AttributeError as e:
        print(f"Caught expected error when modifying read-only property: {e}")

    print("\n--- 3. Defaults & Logic ---")
    tx = Transaction(amount=1250.50, description="Cloud Hosting")
    print(f"Transaction: {tx}")
    print(f"Formatted Amount: {tx.display_amount()}")
    print(f"Timestamp: {tx.timestamp}")
