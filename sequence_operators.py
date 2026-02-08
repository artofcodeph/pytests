"""
Python Sequence Operators & Operations
This guide explains what you can do with strings, lists, and tuples using operators.
"""

# ------------------------------------------------------------------------------
# 1. REPETITION OPERATOR (*)
# ------------------------------------------------------------------------------
print("--- 1. Repetition (*) ---")
# Used for: Creating visual separators, padding, or repeating data patterns.

# String repetition
print("=" * 30)  # Visual separator
print("Go! " * 3) # "Go! Go! Go! "

# List repetition (useful for initializing fixed-size lists)
empty_slots = [0] * 5
print(f"List of 5 zeros: {empty_slots}")

# CAUTION: Mutability with repetition
# [[0]*3]*3 creates a list where every inner list is the SAME object.
# Use list comprehension instead for independent inner lists.
safe_matrix = [[0] * 3 for _ in range(3)]
print(f"Safe Matrix: {safe_matrix}")


# ------------------------------------------------------------------------------
# 2. CONCATENATION OPERATOR (+)
# ------------------------------------------------------------------------------
print("\n--- 2. Concatenation (+) ---")
# Used for: Joining sequences of the same type.

# String join
first = "Hello"
second = "World"
print(first + " " + second)

# List join
list_a = [1, 2]
list_b = [3, 4]
print(list_a + list_b) # [1, 2, 3, 4]


# ------------------------------------------------------------------------------
# 3. MEMBERSHIP OPERATORS (in / not in)
# ------------------------------------------------------------------------------
print("\n--- 3. Membership (in) ---")
# Used for: Fast checks if an item exists in a sequence.

text = "Python is awesome"
print(f"Is 'aw' in text? : {'aw' in text}")

my_list = ["apple", "banana", "cherry"]
print(f"Is 'grape' not in list? : {'grape' not in my_list}")


# ------------------------------------------------------------------------------
# 4. IDENTITY VS EQUALITY (is vs ==)
# ------------------------------------------------------------------------------
print("\n--- 4. Identity (is) vs Equality (==) ---")
# Used for: Checking if two variables point to the same memory object.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}  (Values are the same)")
print(f"a is b: {a is b} (Memory locations are DIFFERENT)")
print(f"a is c: {a is c} (Memory location is the SAME)")


# ------------------------------------------------------------------------------
# 5. UNPACKING OPERATORS (* / **)
# ------------------------------------------------------------------------------
print("\n--- 5. Unpacking (*) ---")
# Used for: Breaking a sequence into individual arguments.

# Capture remaining items
first_item, *middle_items, last_item = [1, 2, 3, 4, 5]
print(f"First: {first_item}, Middle: {middle_items}, Last: {last_item}")

# Merging lists into a new list
list1 = [1, 2]
list2 = [3, 4]
merged = [*list1, *list2, 5]
print(f"Merged with *: {merged}")


# ------------------------------------------------------------------------------
# 6. SLICING REPLACEMENT (Advanced Mutability)
# ------------------------------------------------------------------------------
print("\n--- 6. Slice Assignment ---")
# Used for: Replacing parts of a list in-place.

nums = [1, 2, 3, 4, 5]
nums[1:4] = [10, 20] # Replaces [2, 3, 4] with [10, 20]
print(f"After slice assignment: {nums}")
