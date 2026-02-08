"""
Python Lists Basics - A Comprehensive Guide
Python lists are ordered, mutable, and allow duplicate elements.
"""

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 10, 20]
mixed = [1, "hello", True, 3.14]  # Lists can contain different data types
empty = []

print(f"Initial list: {fruits}")

# 2. Accessing Elements (Indexing)
# Indices start at 0
print(f"First fruit: {fruits[0]}")  # apple
print(f"Last fruit: {fruits[-1]}")  # cherry (Negative indexing starts from the end)

# 3. Slicing Lists (Range of elements)
# Syntax: list[start:end:step]
print(f"First two fruits: {fruits[0:2]}") # ['apple', 'banana'] - end index is exclusive
print(f"Every second number: {numbers[::2]}") # [1, 3, 20]

# 4. Modifying Lists
fruits[1] = "blueberry" # Change an item
print(f"Modified list: {fruits}")

# 5. List Methods
# Adding Items
fruits.append("orange") # Add to the end
fruits.insert(1, "mango") # Insert at specific index
print(f"After adding: {fruits}")

# Removing Items
fruits.remove("apple") # Remove specific value
popped = fruits.pop() # Remove and return last item
del fruits[0] # Remove by index
print(f"After removals: {fruits}")

# 6. Basic Operations
print(f"Length of list: {len(fruits)}") # Count items
print(f"Is 'mango' in fruits? {'mango' in fruits}") # Check existence

# 7. Sorting and Reversing
numbers.sort() # Sort in place
numbers.reverse() # Reverse in place
print(f"Sorted/Reversed numbers: {numbers}")

# 8. List Comprehension (Advanced Basics)
# A concise way to create lists
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")