"""
Python Reflection and Introspection Guide: Observing and Interacting with Objects at Runtime
This script covers id, type, dir, getattr, setattr, and inheritance inspection.
"""

import inspect

def header(text):
    print(f"\n{'='*10} {text} {'='*10}")

def identity_type_guide():
    header("IDENTITY & TYPE")
    x = [1, 2, 3]
    
    # 1. id() - Memory address
    print(f"Memory ID: {id(x)}")
    
    # 2. type() - The class of the object
    print(f"Type: {type(x)}")
    
    # 3. isinstance() - Check if object is an instance of a class (or subclass)
    print(f"Is list? {isinstance(x, list)}")
    print(f"Is object? {isinstance(x, object)}")
    
    # 4. issubclass() - Check inheritance relationship
    print(f"Is list a subclass of object? {issubclass(list, object)}")

def attribute_access_guide():
    header("ATTRIBUTE ACCESS")
    
    class Person:
        def __init__(self, name):
            self.name = name
    
    p = Person("Alice")
    
    # 1. dir() - List all attributes and methods
    print(f"Attributes of p: {dir(p)[:5]}... (truncated)")
    
    # 2. hasattr() - Check if attribute exists
    print(f"Has 'name'? {hasattr(p, 'name')}")
    print(f"Has 'age'? {hasattr(p, 'age')}")
    
    # 3. getattr() - Get attribute value dynamically
    name_val = getattr(p, "name")
    print(f"getattr('name'): {name_val}")
    
    # 4. setattr() - Set attribute value dynamically
    setattr(p, "age", 30)
    print(f"After setattr, age: {p.age}")
    
    # 5. delattr() - Remove attribute
    delattr(p, "age")
    print(f"After delattr, has 'age'? {hasattr(p, 'age')}")

def callable_signature_guide():
    header("CALLABLE & SIGNATURE")
    
    def greet(name: str, age: int = 25) -> str:
        return f"Hello {name}, you are {age}"
    
    # 1. callable() - Check if object can be called
    print(f"Is 'greet' callable? {callable(greet)}")
    print(f"Is '123' callable? {callable(123)}")
    
    # 2. inspect.signature() - Introspect function parameters
    sig = inspect.signature(greet)
    print(f"Signature of greet: {sig}")
    for param_name, param in sig.parameters.items():
        print(f"  Parameter: {param_name}, Default: {param.default}, Type: {param.annotation}")

def inheritance_guide():
    header("INHERITANCE & HIERARCHY")
    
    class A: pass
    class B(A): pass
    class C(B): pass
    
    obj = C()
    
    # 1. __class__ - Reference to the class
    print(f"Object's class: {obj.__class__}")
    
    # 2. __bases__ - Direct base classes
    print(f"Bases of C: {C.__bases__}")
    
    # 3. __mro__ - Method Resolution Order (The inheritance path)
    print(f"MRO of C: {C.__mro__}")

def creative_id_usage():
    header("CREATIVE USES OF id()")
    
    # 1. Detection of Object Re-use (Interning)
    # Small integers and some strings are "interned" for efficiency.
    a = 256
    b = 256
    c = 257
    d = 257
    print(f"256: same id? {id(a) == id(b)}") # True
    print(f"257: same id? {id(c) == id(d)}") # False (usually, depends on context)
    
    # 2. Tracking object progression (is it the SAME object or a copy?)
    original_list = [1, 2, 3]
    modified_list = original_list
    modified_list.append(4)
    copied_list = original_list[:]
    
    print(f"Original vs Modified: same id? {id(original_list) == id(modified_list)}") # True
    print(f"Original vs Copy: same id? {id(original_list) == id(copied_list)}")         # False
    
    # 3. Using id() as a unique key for non-hashable objects in a dict/set
    # This can be useful for graph traversals or registry systems.
    class GraphNode:
        def __init__(self, val): self.val = val
    
    node = GraphNode("A")
    visited = {id(node): "Processed"}
    print(f"Visited node via id: {visited[id(node)]}")

if __name__ == "__main__":
    identity_type_guide()
    creative_id_usage()
    attribute_access_guide()
    callable_signature_guide()
    inheritance_guide()
