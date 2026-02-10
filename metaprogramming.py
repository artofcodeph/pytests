"""
Python Metaprogramming Guide
Metaprogramming is the art of writing code that manipulates, creates, or manages other code.
"""

import functools

# ==============================================================================
# 1. DECORATORS (The Most Common Metaprogramming)
# ==============================================================================
print("--- 1. Decorators ---")

def debug_log(func):
    """A decorator that logs function calls and arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug_log
def add(a, b):
    return a + b

add(5, 10)


# ==============================================================================
# 2. DYNAMIC CLASS CREATION (Using type())
# ==============================================================================
print("\n--- 2. Dynamic Class Creation (type()) ---")

# type(name, bases, dict)
# name: string of class name
# bases: tuple of parent classes
# dict: dictionary of attributes and methods

def greet(self):
    print(f"Hello, I am a {self.__class__.__name__} instance!")

DynamicRobot = type("DynamicRobot", (object,), {"greet": greet, "version": 1.0})

robot = DynamicRobot()
robot.greet()
print(f"Robot version: {robot.version}")


# ==============================================================================
# 3. METACLASSES (The 'Class of a Class')
# ==============================================================================
print("\n--- 3. Metaclasses ---")

class SingletonMeta(type):
    """A metaclass that implements the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing Database Connection...")

db1 = Database()
db2 = Database()
print(f"db1 is db2? {db1 is db2} (Both are the SAME instance)")


# ==============================================================================
# 4. __init_subclass__ (Modern Alternative to Metaclasses)
# ==============================================================================
print("\n--- 4. __init_subclass__ ---")

class PluginBase:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Automatically register any subclass created
        print(f"Registering new plugin: {cls.__name__}")
        cls.registry.append(cls)

class WeatherPlugin(PluginBase): pass
class StockPlugin(PluginBase): pass

print(f"Registered Plugins: {[p.__name__ for p in PluginBase.registry]}")


# ==============================================================================
# 5. DYNAMIC ATTRIBUTE HANDLING (__getattr__)
# ==============================================================================
print("\n--- 5. Dynamic Attribute Handling ---")

class FlexibleObject:
    """An object that handles undefined attributes gracefully."""
    def __getattr__(self, name):
        # Called ONLY when an attribute isn't found standardly
        return f"Attribute '{name}' not found, but I handled it!"

obj = FlexibleObject()
print(obj.some_missing_property)


# ==============================================================================
# SUMMARY: WHEN TO USE METAPROGRAMMING?
# ==============================================================================
"""
MOTIVATION:
1. Don't Repeat Yourself (DRY): If you find yourself writing the same logic across 
   100 classes, use a metaclass or __init_subclass__ to automate it.
2. Framework Building: Popular tools like Django (ORM) and Flask use 
   metaprogramming extensively to turn simple declarations into complex behavior.
3. Rule of Thumb: If you can solve it with normal classes or functions, do that. 
   Metaprogramming is a 'power tool'—powerful, but complex to maintain.
"""
