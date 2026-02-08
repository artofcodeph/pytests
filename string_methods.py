"""
Python String Test Methods (Predicate Functions)
These methods return True or False based on the content of a string.
"""

def test_string(s, label):
    print(f"\n--- Testing String: '{s}' ({label}) ---")
    
    # Core Test Methods
    tests = {
        "s.isalpha()": s.isalpha(),      # True if all characters are letters
        "s.isdigit()": s.isdigit(),      # True if all characters are digits
        "s.isalnum()": s.isalnum(),      # True if all characters are letters OR digits
        "s.islower()": s.islower(),      # True if all cased characters are lowercase
        "s.isupper()": s.isupper(),      # True if all cased characters are uppercase
        "s.istitle()": s.istitle(),      # True if string follows "Title Case"
        "s.isspace()": s.isspace(),      # True if all characters are whitespace
        "s.isascii()": s.isascii(),      # True if all characters are ASCII (0-127)
        "s.isprintable()": s.isprintable() # True if all characters are printable (not \n, \t)
    }
    
    for method, result in tests.items():
        print(f"{method:<18} : {result}")

# 1. Standard Alpha
test_string("Python", "Alpha Only")

# 2. Digits
test_string("12345", "Digits Only")

# 3. Alphanumeric
test_string("Python3", "Mixed")

# 4. Whitespace
test_string("  \t\n  ", "Whitespace Only")

# 5. Specialized Numeric Tests
print("\n" + "="*50)
print("DEEP DIVE: isdecimal() vs isdigit() vs isnumeric()")
print("="*50)

# Example: Unicode fractions and superscript
s_numeric = "½"
s_digit = "²"
s_plain = "5"

def compare_numerics(s, name):
    print(f"\nString: '{s}' ({name})")
    print(f"  .isdecimal(): {s.isdecimal()}") # Only standard decimal digits (0-9)
    print(f"  .isdigit():   {s.isdigit()}")   # standard + subscripts/superscripts
    print(f"  .isnumeric(): {s.isnumeric()}") # standard + superscripts + fractions (like ½)

compare_numerics(s_plain, "Plain Digit")
compare_numerics(s_digit, "Superscript Two")
compare_numerics(s_numeric, "Fraction One Half")

"""
SUMMARY TABLE:
- isdecimal(): Strictly standard 0-9 digits.
- isdigit():   Decimal digits + special digit chars (like exponents ²).
- isnumeric(): Everything above + fractions, roman numerals, and numeric chars from other languages.
"""

# ==============================================================================
# COMPREHENSIVE STRING OPERATIONS GUIDE
# ==============================================================================
print("\n" + "="*50)
print("PART 2: COMMON & ADVANCED STRING OPERATIONS")
print("="*50)

# 1. SLICING (SUBSTRINGS)
print("\n1. Slicing & Substrings (s[start:stop:step])")
s = "Python Programming"
# Motivation: Used for extracting specific parts of a string without modification.
print(f"Original:   '{s}'")
print(f"s[0:6]:     '{s[0:6]}'    (First 6 chars)")
print(f"s[7:]:      '{s[7:]}'     (From index 7 to end)")
print(f"s[:6]:      '{s[:6]}'     (Up to index 6)")
print(f"s[-11:]:    '{s[-11:]}'   (Last 11 chars using negative indexing)")
print(f"s[::2]:     '{s[::2]}'    (Every second character)")
print(f"s[::-1]:    '{s[::-1]}'   (Reverse the string)")

# 2. SEARCHING & COUNTING
print("\n2. Searching & Counting")
text = "The quick brown fox jumps over the lazy dog"
# .find(): Returns index of first occurrence, or -1 if not found.
# Use for simple presence checks where you need the position.
print(f"find('fox'):   {text.find('fox')}") 
# .index(): Same as find() but raises ValueError if not found.
# Use when you ARE SURE the substring exists.
print(f"index('fox'):  {text.index('fox')}")
# .count(): Counts non-overlapping occurrences.
# Use for frequency analysis.
print(f"count('e'):    {text.count('e')}")
# .startswith() / .endswith(): Boolean checks.
# Much more readable than slicing s[:5] == 'start'.
print(f"startswith('The'): {text.startswith('The')}")
print(f"endswith('dog'):   {text.endswith('dog')}")

# 3. SPLITTING & JOINING
print("\n3. Splitting & Joining")
data = "apple,banana,cherry,date"
# .split(): Converts string to list based on delimiter.
# Essential for CSV or log parsing.
fruits = data.split(",")
print(f"split(','):   {fruits}")
# .join(): Recombines list into string with a separator.
# MUCH faster than concatenating strings with '+' in a loop.
print(f"join(' | '):  {' | '.join(fruits)}")
# .splitlines(): Splits by line breaks (\n, \r).
multiline = "Line 1\nLine 2\r\nLine 3"
print(f"splitlines(): {multiline.splitlines()}")

# 4. TRANSFORMATION & CLEANING
print("\n4. Transformation & Cleaning")
messy = "   ---Hello World---   "
# .strip(): Removes whitespace (or specific chars) from BOTH ends.
print(f"strip():      '{messy.strip()}'")
print(f"strip(' - '): '{messy.strip(' - ')}'")
# .replace(old, new): Global replacement.
print(f"replace():    '{text.replace('fox', 'cat')}'")
# .title() / .capitalize(): Formatting.
print(f"title():      'python is fun'.title() -> '{'python is fun'.title()}'")
# .casefold(): Aggressive lowercase for caseless matching (better than .lower()).
print(f"casefold():   'ß'.casefold() -> '{'ß'.casefold()}' (Standard 'ss')")

# 5. ALIGNMENT & PADDING
print("\n5. Alignment & Padding")
# Use for terminal UI formatting or fixed-width text files.
print(f"center(20):   '|{'Hi'.center(20)}|'")
print(f"ljust(20):    '|{'Hi'.ljust(20)}|'")
print(f"rjust(20):    '|{'Hi'.rjust(20)}|'")
print(f"zfill(5):     '{'42'.zfill(5)}' (Zero padding for numbers)")

# 6. ADVANCED MANIPULATION
print("\n6. Advanced Manipulation")
# .partition(): Returns (before, sep, after). Guaranteed 3-tuple.
# Use instead of split() if you only care about the FIRST split point.
url = "https://example.com/page"
print(f"partition('://'): {url.partition('://')}")

# .removeprefix() / .removesuffix(): (Python 3.9+)
# Safer than slicing because it only removes if the prefix/suffix matches.
filename = "report_2023.pdf"
print(f"removesuffix():   '{filename.removesuffix('.pdf')}'")

# .translate() & .maketrans(): Bulk character replacement.
# Extremely efficient for multiple single-char swaps (e.g. DNA/RNA mapping).
trans_map = str.maketrans("ABC", "123")
print(f"translate():      'CABBA'.translate(trans_map) -> '{'CABBA'.translate(trans_map)}'")
