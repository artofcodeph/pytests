"""
Guide: Python Dataclasses (@dataclass)
This script demonstrates how to use the dataclasses module to create 
concise, readable data containers with minimal boilerplate.
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional
from datetime import datetime

@dataclass(frozen=True) # frozen=True makes the instance immutable (read-only)
class User:
    """Basic dataclass with type hints and default values."""
    id: int
    username: str
    email: str
    is_active: bool = True
    # For mutable defaults like lists, use field(default_factory=...)
    tags: List[str] = field(default_factory=list)
    
    # __post_init__ is used for validation or processing after the generated __init__
    def __post_init__(self):
        # Note: If frozen=True, you must use object.__setattr__ to modify fields here
        if "@" not in self.email:
            # This is a bit tricky with frozen=True, but usually validation happens before
             print(f"Warning: Invalid email format for {self.username}")

@dataclass
class Transaction:
    """A dataclass representing a financial transaction."""
    amount: float
    description: str
    timestamp: datetime = field(default_factory=datetime.now)
    
    def display_amount(self):
        return f"${self.amount:,.2f}"

if __name__ == "__main__":
    print("--- 1. Basic Dataclass Usage ---")
    u1 = User(id=1, username="arthur", email="arthur@example.com", tags=["python", "dev"])
    u2 = User(id=1, username="arthur", email="arthur@example.com", tags=["python", "dev"])
    
    # Automatic __repr__
    print(f"User 1: {u1}")
    
    # Automatic __eq__ (equality check based on values, not memory address)
    print(f"u1 == u2: {u1 == u2}") 

    print("\n--- 2. Immutability (frozen=True) ---")
    try:
        u1.username = "modified"
    except Exception as e:
        print(f"Caught expected error when modifying frozen dataclass: {e}")

    print("\n--- 3. Conversion Utilities ---")
    print(f"As Dictionary: {asdict(u1)}")
    print(f"As Tuple: {astuple(u1)}")

    print("\n--- 4. Defaults & Factories ---")
    tx = Transaction(amount=1250.50, description="Cloud Hosting")
    print(f"Transaction: {tx}")
    print(f"Formatted Amount: {tx.display_amount()}")
    print(f"Timestamp: {tx.timestamp}")
