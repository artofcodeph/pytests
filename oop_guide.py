"""
Object-Oriented Programming (OOP) Guide - Advanced & Pythonic
This script demonstrates the core and advanced principles of OOP in Python:
1. Classes and Objects
2. Inheritance & Abstract Base Classes (ABCs)
3. Polymorphism
4. Encapsulation via Properties (@property)
5. Dunder (Magic) Methods for Pythonic behavior
6. Composition & Protocols
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    """
    Abstract Base Class for all animals.
    Using ABC ensures that we cannot instantiate Animal directly
    and that subclasses MUST implement abstract methods.
    """
    species = "Unknown"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self._age = age        # Protected attribute for use with property
        self._is_alive = True

    @abstractmethod
    def speak(self):
        """Abstract method to be implemented by subclasses."""
        pass

    @property
    def age(self):
        """The age property (Getter)."""
        return self._age

    @age.setter
    def age(self, value):
        """Property Setter with validation - Pythonic encapsulation."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    def describe(self):
        """Common method for all animals."""
        return f"{self.name} is {self.age} years old."

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Factory method using @classmethod."""
        age = datetime.now().year - birth_year
        return cls(name, age)

    def __str__(self):
        """Dunder method for user-friendly string representation."""
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"

    def __repr__(self):
        """Dunder method for developer-friendly representation."""
        return f"<{self.__class__.__name__} name={self.name} age={self.age}>"

class Dog(Animal):
    """Subclass representing a dog."""
    species = "Canine"
    
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

class Cat(Animal):
    """Subclass representing a cat."""
    species = "Feline"

    def speak(self, sound="Meow"):
        return f"{self.name} says {sound}"

class Zoo:
    """
    Composition Example.
    A Zoo is NOT an Animal, but it DOES HAVE Animals.
    Implements container protocols to be 'Pythonic'.
    """
    def __init__(self, name):
        self.name = name
        self._animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            raise TypeError("Can only add instances of Animal subclasses")

    # Pythonic Protocol: Iteration
    def __iter__(self):
        return iter(self._animals)

    # Pythonic Protocol: Length
    def __len__(self):
        return len(self._animals)

    # Pythonic Protocol: Indexing
    def __getitem__(self, index):
        return self._animals[index]

    def __str__(self):
        return f"Zoo '{self.name}' with {len(self)} animals"

def animal_concert(animals):
    """Demonstrates polymorphism."""
    print("\n--- Animal Concert ---")
    for animal in animals:
        # Implicitly uses __str__ when printing the object
        print(f"{animal}: {animal.speak()}")

if __name__ == "__main__":
    # 1. Factory method & Inheritance
    tagpi = Dog.from_birth_year("Tagpi", 2020)
    garfield = Cat("Garfield", 3)

    # 2. Properties and Validation
    print(f"Original age: {tagpi.age}")
    tagpi.age = 6  # Uses setter
    print(f"Updated age: {tagpi.age}")
    
    try:
        tagpi.age = -1
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # 3. Composition & Protocols (The Zoo)
    my_zoo = Zoo("Happy Pets")
    my_zoo.add_animal(tagpi)
    my_zoo.add_animal(garfield)

    print(f"\n{my_zoo}")
    print(f"First animal in zoo: {my_zoo[0]}") # Uses __getitem__
    
    # 4. Polymorphism & Iteration
    # animal_concert works with any list-like or iterable of Animals
    animal_concert(my_zoo) # my_zoo is iterable due to __iter__

    # 5. Legacy logic preserved
    def calculate_force(mass, acc):
        return mass * acc
    print(f"\nForce Calculation (legacy logic): {calculate_force(9, 7)}")
