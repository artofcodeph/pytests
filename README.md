# Python Learning Laboratory (python-tests)

A collection of high-quality Python guides, scripts, and tests designed for mastering core language concepts, from basic collections to advanced metaprogramming.

## 📂 Repository Contents

### 🎓 Educational Guides
Comprehensive, well-commented scripts that explain key Python features:

- **[collections_guide.py](collections_guide.py)**: Deep dive into Lists, Sets, Dictionaries, and Tuples, including advanced techniques like NamedTuples and DefaultDicts.
- **[reflection_introspection_guide.py](reflection_introspection_guide.py)**: Mastery of `id()`, `type()`, `getattr()`, and runtime object investigation.
- **[comprehensions.py](comprehensions.py)** / **[list_comprehensions.py](list_comprehensions.py)**: Efficiently generating sequences using list, dict, and set comprehensions.
- **[string_methods.py](string_methods.py)**: Exploration of built-in string manipulation power.
- **[sequence_operators.py](sequence_operators.py)**: Understanding slices, indexing, and iteration protocols.

### 🧠 Advanced Concepts
Exploring the boundaries of the Python language:

- **[metaprogramming.py](metaprogramming.py)**: Introduction to decorators, metaclasses, and dynamic class creation.
- **[lamda_functions.py](lamda_functions.py)**: Use cases for anonymous functions and functional programming patterns.
- **[hash_tester.py](hash_tester.py)**: Investigating object hashability and dictionary key requirements.

### 🌐 Network & APIs
- **[api_network_demo.py](api_network_demo.py)**: REST API consumption (GET/POST/PUT/DELETE), `urllib` vs `requests`, thread pool concurrency, retry logic with exponential backoff, and network error handling.

### 🧪 Misc & OOP
- **[employee_oop_demo.py](employee_oop_demo.py)**: Production-grade OOP demonstration covering encapsulation, validation, dunder methods, composition, and mixins.
- **[oop_guide.py](oop_guide.py)**: Comprehensive guide to Object-Oriented Programming (Classes, Inheritance, and Polymorphism).
- **[types_demo.py](types_demo.py)**: Type checking and boolean introspection.
- **[main_file.py](main_file.py)**: General testing ground for ephemeral ideas.

## 🚀 Getting Started on a New Machine

When cloning the repository to another computer, follow these standard steps:

### 1. Clone the repository
```bash
git clone <repository_url>
cd pytests
```

### 2. Set up a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate      # On macOS/Linux
# or: .venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the script
```bash
python api_network_demo.py
```

## 🛠️ Requirements
- Python 3.9+
- Dependencies listed in `requirements.txt` (`requests`)
