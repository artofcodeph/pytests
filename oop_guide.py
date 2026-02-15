"""
Object-Oriented Programming (OOP) Guide
This script demonstrates the core principles of OOP in Python:
1. Classes and Objects
2. Inheritance
3. Polymorphism
4. Encapsulation (naming conventions)
5. Class vs Instance attributes
"""

class Animal:
    """Base class for all animals."""
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
        self._is_alive = True # Protected attribute (convention)

    def speak(self):
        """Placeholder method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

    def describe(self):
        """Common method for all animals."""
        return f"{self.name} is {self.age} years old."

class Dog(Animal):
    """Subclass representing a dog."""
    
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

class Cat(Animal):
    """Subclass representing a cat."""
    species = "Feline" # Overriding class attribute

    def speak(self, sound="Meow"):
        return f"{self.name} says {sound}"

def animal_concert(animals):
    """Demonstrates polymorphism by calling the same method on different objects."""
    print("\n--- Animal Concert ---")
    for animal in animals:
        print(f"{animal.describe()} - {animal.speak()}")

if __name__ == "__main__":
    # Create instances
    tagpi = Dog("Tagpi", 5)
    garfield = Cat("Garfield", 3)

    # Demonstrate basic inheritance and methods
    print(tagpi.describe())
    print(tagpi.speak())
    print(tagpi.fetch("ball"))

    print(garfield.describe())
    print(garfield.speak())

    # Demonstrate Class vs Instance attributes
    print(f"\n{tagpi.name} is a {tagpi.species}")
    print(f"{garfield.name} is a {garfield.species}")

    # Demonstrate Polymorphism
    my_pets = [tagpi, garfield]
    animal_concert(my_pets)

    # Demonstrating the previous functionality from my_dog.py
    def calculate_force(mass, acc):
        """Calculates force (F = m * a)"""
        return mass * acc

    print(f"\nForce Calculation (legacy logic): {calculate_force(9, 7)}")
