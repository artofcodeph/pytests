"""
Python Collections Guide: Basic Operations and Advanced Techniques
This script covers Lists, Sets, Dictionaries, and Tuples.
"""

from collections import namedtuple, defaultdict

def header(text):
    print(f"\n{'='*10} {text} {'='*10}")

def list_guide():
    header("LISTS")
    # Basic Operations
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")          # Add to end
    fruits.insert(1, "blueberry") # Insert at index
    fruits.remove("banana")        # Remove by value
    popped = fruits.pop()          # Remove and return last element
    print(f"Basic List: {fruits}, Popped: {popped}")
    
    # Advanced Techniques
    # 1. List Comprehensions
    squares = [x**2 for x in range(5)]
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Squares: {squares}")
    
    # 2. Slicing Tricks
    rev = fruits[::-1] # Reverse list
    print(f"Reversed: {rev}")
    
    # 3. Zip and Enumerate
    for i, val in enumerate(fruits):
        print(f"Index {i}: {val}")
        
    prices = [1.2, 0.5, 2.0]
    for name, price in zip(fruits, prices):
        print(f"{name} costs ${price}")

def set_guide():
    header("SETS")
    # Basic Operations
    s1 = {1, 2, 3, 3, 4} # Note: Duplicates are removed
    s1.add(5)
    s1.discard(1)
    print(f"Basic Set: {s1}")
    
    # Advanced: Mathematical Operations
    s2 = {4, 5, 6, 7}
    print(f"Union (|): {s1 | s2}")
    print(f"Intersection (&): {s1 & s2}")
    print(f"Difference (-): {s1 - s2}")
    print(f"Symmetric Difference (^): {s1 ^ s2}")
    
    # Set Comprehension
    char_set = {c.upper() for c in "abracadabra" if c not in "abc"}
    print(f"Set Comprehension: {char_set}")

def dict_guide():
    header("DICTIONARIES")
    # Basic Operations
    user = {"name": "Alice", "age": 25}
    user["email"] = "alice@example.com"
    del user["age"]
    print(f"Basic Dict: {user}")
    
    # Advanced Techniques
    # 1. Safe access with default
    print(f"Phone: {user.get('phone', 'Not Found')}")
    
    # 2. Dictionary Comprehension
    prices = {"apple": 0.5, "banana": 0.3, "cherry": 0.8}
    expensive_fruits = {k: v for k, v in prices.items() if v > 0.4}
    print(f"Expensive Fruits: {expensive_fruits}")
    
    # 3. Merging (Python 3.9+)
    extra_info = {"city": "New York", "name": "Alice Smith"}
    merged = user | extra_info # Overwrites common keys with right-hand dict
    print(f"Merged: {merged}")
    
    # 4. Defaultdict
    d = defaultdict(list)
    d['tasks'].append("Clean room")
    print(f"Defaultdict: {dict(d)}")

def tuple_guide():
    header("TUPLES")
    # Basic Operations
    point = (10, 20)
    # point[0] = 5 # This would raise TypeError (immutable)
    print(f"Basic Tuple: {point}")
    
    # Advanced Techniques
    # 1. Unpacking
    x, y = point
    print(f"Unpacked: x={x}, y={y}")
    
    # 2. Packing with * (Extended Iterables Unpacking)
    first, *middle, last = (1, 2, 3, 4, 5)
    print(f"First: {first}, Middle: {middle}, Last: {last}")
    
    # 3. Namedtuples
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(15, 25)
    print(f"NamedTuple: x={p.x}, y={p.y}")

if __name__ == "__main__":
    list_guide()
    set_guide()
    dict_guide()
    tuple_guide()
