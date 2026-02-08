def is_hashable(obj):
    """
    Tests if an object is hashable by attempting to call hash() on it.
    Hashable objects can be used as dictionary keys and set elements.
    """
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# --- Testing the function ---
test_cases = [
    ("banana", "String"),
    (42, "Integer"),
    ((1, 2, 3), "Tuple (Immutable)"),
    ([1, 2, 3], "List (Mutable)"),
    ({"key": "value"}, "Dictionary (Mutable)"),
    ({1, 2, 3}, "Set (Mutable)"),
    (None, "NoneType")
]

print(f"{'Object Type':<20} | {'Is Hashable?':<12}")
print("-" * 35)

for obj, description in test_cases:
    result = is_hashable(obj)
    print(f"{description:<20} | {str(result):<12}")
