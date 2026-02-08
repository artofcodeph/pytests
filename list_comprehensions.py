"""
Comprehensive Guide to Comprehensions & Generators in Python
This script covers Lists, Sets, Dictionaries, and Generators.
"""

import math

# ==========================================
# 1. ADVANCED LIST COMPREHENSIONS
# ==========================================
print("--- Advanced List Comprehensions ---")

# A. Multiple 'if' conditions
# Numbers divisible by both 2 and 3
div_by_6 = [x for x in range(50) if x % 2 == 0 if x % 3 == 0]
print(f"Divisible by 2 & 3: {div_by_6}")

# B. Nested Loops: Cartesian Product
# All possible combinations of two lists
colors = ["red", "green"]
objects = ["car", "bike"]
combinations = [(color, obj) for color in colors for obj in objects]
print(f"Combinations: {combinations}")

# C. Matrix Transposition
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"Transposed Matrix: {transposed}")


# ==========================================
# 2. SET COMPREHENSIONS
# ==========================================
# Sets use {} and automatically handle uniqueness.
print("\n--- Set Comprehensions ---")

# A. Extract unique vowels from a text
sentence = "python programming is fun and powerful"
vowels = {char for char in sentence if char in "aeiou"}
print(f"Unique vowels: {vowels}")

# B. Performing operations on elements
# Set of square roots (floored) for unique numbers
nums = [1, 4, 9, 16, 16, 25]
roots = {int(math.sqrt(n)) for n in nums}
print(f"Unique roots: {roots}")


# ==========================================
# 3. DICTIONARY COMPREHENSIONS
# ==========================================
# Format: {key: value for item in iterable}
print("\n--- Dictionary Comprehensions ---")

# A. Creating a mapping of numbers to their cubes
cubes = {x: x**3 for x in range(1, 6)}
print(f"Cubes Mapping: {cubes}")

# B. Filtering a dictionary
stock = {"apple": 20, "banana": 4, "cherry": 15, "date": 0}
available_stock = {item: count for item, count in stock.items() if count > 0}
print(f"Available Stock: {available_stock}")

# C. Character Frequency Counter
# Count how many times each character appears in a string
text = "banana"
char_counts = {char: text.count(char) for char in set(text)}
print(f"Character counts in '{text}': {char_counts}") # {'b': 1, 'n': 2, 'a': 3}

# D. Conditional Values
# Tag scores as Pass/Fail
scores = {"Alice": 85, "Bob": 40, "Charlie": 72}
results = {name: ("Pass" if score >= 50 else "Fail") for name, score in scores.items()}
print(f"Results: {results}")


# ==========================================
# 4. GENERATOR EXPRESSIONS
# ==========================================
# Generators use () and are "lazy" - they don't store the whole list in memory.
print("\n--- Generator Expressions ---")

# A. Sum of squares (memory efficient)
# This calculates one number at a time then discards it, instead of building a list.
sum_squares = sum(x**2 for x in range(1000000)) 
print(f"Sum of 1M squares: {sum_squares}")

# B. Iterating through a generator
gen = (math.factorial(x) for x in range(5))
print("Factorials via generator:", end=" ")
for val in gen:
    print(val, end=" ")
print("\n")

# C. Comparison: List vs Generator
import sys
list_comp = [x for x in range(10000)]
gen_exp = (x for x in range(10000))
print(f"Memory size of List: {sys.getsizeof(list_comp)} bytes")
print(f"Memory size of Generator: {sys.getsizeof(gen_exp)} bytes")
