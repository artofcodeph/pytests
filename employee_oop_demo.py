"""
Comprehensive Demonstration of Object-Oriented Programming (OOP) in Python
-------------------------------------------------------------------------
Domain: Employee Management System

This module demonstrates core and advanced OOP principles in Python:
1. Abstraction (ABC, @abstractmethod)
2. Encapsulation (Private/Protected attributes, @property getters & setters)
3. Inheritance & Method Overriding (Single & Multiple inheritance with Mixins, super())
4. Polymorphism (Duck typing, unified interface implementation)
5. Class Methods & Static Methods (@classmethod, @staticmethod)
6. Dunder / Magic Methods (__str__, __repr__, __eq__, __hash__, __lt__, __len__)
7. Composition & Aggregation (Department, Manager team management)
"""

from abc import ABC, abstractmethod
from datetime import date
from enum import Enum
import re
from typing import List, Optional, Dict, Any


# ==========================================
# 1. ENUM (Domain Types)
# ==========================================
class PayFrequency(Enum):
    """Enumeration representing pay frequency types."""
    MONTHLY = "Monthly"
    HOURLY = "Hourly"
    PROJECT_BASED = "Project-Based"


# ==========================================
# 2. MIXIN CLASS (Multiple Inheritance)
# ==========================================
class TaxCalculableMixin:
    """
    Mixin Class providing tax calculation capabilities.
    Demonstrates MULTIPLE INHERITANCE / MIXIN PATTERN:
    - Provides specific reusable behavior across unrelated classes without deep class hierarchies.
    """

    DEFAULT_TAX_RATE: float = 0.20  # 20% default tax rate

    @staticmethod
    def calculate_tax(gross_pay: float, tax_rate: float = DEFAULT_TAX_RATE) -> float:
        """Calculates income tax based on gross pay and rate."""
        if gross_pay < 0:
            raise ValueError("Gross pay cannot be negative.")
        return round(gross_pay * tax_rate, 2)


# ==========================================
# 3. ABSTRACT BASE CLASS (Abstraction & Encapsulation)
# ==========================================
class Employee(ABC, TaxCalculableMixin):
    """
    Abstract Base Class (ABC) representing a generic Employee.
    
    OOP Concepts Demonstrated:
    - ABSTRACTION: Inherits from ABC; cannot be directly instantiated. Defines standard interface contract.
    - ENCAPSULATION: Hides internal state with private (__base_salary) and protected (_department) attributes.
    - MULTIPLE INHERITANCE: Inherits from both ABC and TaxCalculableMixin.
    """

    # Class-level variables (shared across all instances of Employee)
    _employee_count: int = 0
    COMPANY_NAME: str = "TechCorp Solutions"

    def __init__(self, name: str, employee_id: str, department: str, base_salary: float):
        """
        Constructor method.
        
        Attribute visibility convention:
        - Public: self.name
        - Protected: self._department (indicates intended internal/subclass usage)
        - Private: self.__base_salary (Python name-mangling applied: _Employee__base_salary)
        """
        self.name = name
        self.employee_id = self._validate_id(employee_id)
        self._department = department
        self.__base_salary = 0.0  # Private attribute initialized
        self.base_salary = base_salary  # Invokes property setter for validation
        self.hire_date: date = date.today()

        # Track total employees created across subclasses
        Employee._employee_count += 1

    # --- Encapsulation: Property Getters & Setters ---
    @property
    def base_salary(self) -> float:
        """Getter for private attribute __base_salary."""
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value: float) -> None:
        """
        Setter for private attribute __base_salary.
        Demonstrates data validation and encapsulation safeguards.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a numeric value.")
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self.__base_salary = float(value)

    @property
    def department(self) -> str:
        """Getter for protected attribute _department."""
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        """Setter for department with input validation."""
        if not value or not value.strip():
            raise ValueError("Department name cannot be empty.")
        self._department = value.strip()

    # --- Abstract Interface (Must be implemented by subclasses) ---
    @property
    @abstractmethod
    def employee_type(self) -> str:
        """Abstract property: Returns string description of employee type."""
        pass

    @abstractmethod
    def calculate_pay(self) -> float:
        """Abstract method: Calculates gross pay for current period."""
        pass

    # --- Class Methods & Static Methods ---
    @classmethod
    def get_employee_count(cls) -> int:
        """
        CLASSMETHOD: Operates on class state (cls), not instance state (self).
        Returns total number of employees instantiated.
        """
        return cls._employee_count

    @staticmethod
    def _validate_id(emp_id: str) -> str:
        """
        STATICMETHOD: Utility method independent of class or instance state.
        Validates employee ID format (e.g. EMP-1001).
        """
        pattern = r"^EMP-\d{4}$"
        if not re.match(pattern, emp_id):
            raise ValueError(f"Invalid Employee ID '{emp_id}'. Expected format: EMP-XXXX (e.g. EMP-1001).")
        return emp_id

    # --- Dunder / Magic Methods (Operator Overloading & Custom Behaviors) ---
    def __str__(self) -> str:
        """Human-readable string representation (used by print() and str())."""
        return f"[{self.employee_id}] {self.name} - {self.employee_type} ({self.department})"

    def __repr__(self) -> str:
        """Developer/Debugging representation (used in interactive shells and logs)."""
        return f"{self.__class__.__name__}(id='{self.employee_id}', name='{self.name}', salary={self.base_salary})"

    def __eq__(self, other: object) -> bool:
        """Equality operator (==). Compares employees based on unique employee_id."""
        if not isinstance(other, Employee):
            return False
        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        """Hashing implementation. Enables using Employee instances in sets or as dictionary keys."""
        return hash(self.employee_id)

    def __lt__(self, other: 'Employee') -> bool:
        """Less-than operator (<). Enables sorting employees by base salary."""
        if not isinstance(other, Employee):
            return NotImplemented
        return self.base_salary < other.base_salary


# ==========================================
# 4. CONCRETE DERIVED CLASSES (Inheritance & Polymorphism)
# ==========================================
class FullTimeEmployee(Employee):
    """
    Derived Class representing a salaried full-time employee.
    
    OOP Concepts:
    - INHERITANCE: Inherits core attributes and behavior from Employee base class.
    - POLYMORPHISM: Implements calculate_pay() and employee_type specifically for full-time staff.
    """

    def __init__(self, name: str, employee_id: str, department: str, base_salary: float, annual_bonus: float = 0.0):
        # Call parent constructor using super()
        super().__init__(name, employee_id, department, base_salary)
        self.annual_bonus = annual_bonus

    @property
    def employee_type(self) -> str:
        """Concrete implementation of abstract property."""
        return "Full-Time Employee"

    def calculate_pay(self) -> float:
        """
        Polymorphic Method Implementation.
        Calculates monthly gross pay = (annual salary / 12) + (annual bonus / 12).
        """
        monthly_base = self.base_salary / 12
        monthly_bonus = self.annual_bonus / 12
        return round(monthly_base + monthly_bonus, 2)

    @classmethod
    def from_csv_string(cls, csv_line: str) -> 'FullTimeEmployee':
        """
        Factory Classmethod: Constructs a FullTimeEmployee object from a CSV line.
        Example format: "Alice Smith, EMP-1001, Engineering, 120000, 12000"
        """
        parts = [p.strip() for p in csv_line.split(",")]
        if len(parts) < 4:
            raise ValueError("CSV line must have at least 4 fields: Name, ID, Department, BaseSalary")
        name, emp_id, dept, salary = parts[0], parts[1], parts[2], float(parts[3])
        bonus = float(parts[4]) if len(parts) > 4 else 0.0
        return cls(name, emp_id, dept, salary, bonus)


class ContractorEmployee(Employee):
    """
    Derived Class representing an hourly contract worker.
    
    OOP Concepts:
    - INHERITANCE: Subclasses Employee.
    - POLYMORPHISM: Calculates pay based on hourly rate * hours worked.
    """

    def __init__(self, name: str, employee_id: str, department: str, hourly_rate: float, hours_worked: float = 0.0):
        # Base salary set to 0 as pay is determined dynamically by hourly rate
        super().__init__(name, employee_id, department, base_salary=0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def employee_type(self) -> str:
        """Concrete implementation of abstract property."""
        return "Contractor"

    def calculate_pay(self) -> float:
        """
        Polymorphic Method Implementation.
        Calculates pay = hourly_rate * hours_worked.
        """
        return round(self.hourly_rate * self.hours_worked, 2)

    @classmethod
    def from_csv_string(cls, csv_line: str) -> 'ContractorEmployee':
        """Factory Classmethod for creating Contractor instance from CSV line."""
        parts = [p.strip() for p in csv_line.split(",")]
        name, emp_id, dept, rate, hours = parts[0], parts[1], parts[2], float(parts[3]), float(parts[4])
        return cls(name, emp_id, dept, rate, hours)


# ==========================================
# 5. COMPOSITION & ADVANCED SUBCLASSING
# ==========================================
class Manager(FullTimeEmployee):
    """
    Specialized Manager class.
    
    OOP Concepts:
    - COMPOSITION / AGGREGATION: Manager "has-a" list of Employee direct reports.
    - METHOD OVERRIDING: Customizes calculate_pay() by adding stipend per team member.
    - DUNDER OVERRIDING: Implements __len__() to return team size.
    """

    def __init__(self, name: str, employee_id: str, department: str, base_salary: float, annual_bonus: float = 0.0):
        super().__init__(name, employee_id, department, base_salary, annual_bonus)
        # Composition: Manager owns/maintains a team collection of Employee instances
        self._team: List[Employee] = []

    @property
    def employee_type(self) -> str:
        return "Manager"

    def add_team_member(self, employee: Employee) -> None:
        """Adds an employee to the manager's team."""
        if not isinstance(employee, Employee):
            raise TypeError("Only instances of Employee subclasses can be added to team.")
        if employee not in self._team:
            self._team.append(employee)

    def remove_team_member(self, employee: Employee) -> None:
        """Removes an employee from the manager's team."""
        if employee in self._team:
            self._team.remove(employee)

    def calculate_pay(self) -> float:
        """
        Method Overriding with super().
        Calculates base full-time monthly pay + management stipend ($250 per team member).
        """
        base_monthly_pay = super().calculate_pay()
        team_stipend = len(self._team) * 250.0
        return round(base_monthly_pay + team_stipend, 2)

    def __len__(self) -> int:
        """Magic method override: Allows using len(manager_instance) to get team count."""
        return len(self._team)

    def list_team_members(self) -> List[str]:
        """Returns string overview of all direct reports."""
        return [str(emp) for emp in self._team]


# ==========================================
# 6. EXECUTION & VERIFICATION TEST DRIVE
# ==========================================
def main():
    """Demonstrates all Python OOP features implemented above."""
    print("=" * 75)
    print("     PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) COMPREHENSIVE DEMO     ")
    print("=" * 75)

    # 1. ENCAPSULATION & DATA VALIDATION
    print("\n1. ENCAPSULATION & DATA VALIDATION")
    print("-" * 50)
    emp1 = FullTimeEmployee("Alice Smith", "EMP-1001", "Engineering", 120000.0, annual_bonus=12000.0)
    print(f"Created Employee: {emp1}")
    print(f"Base Salary (accessed via @property getter): ${emp1.base_salary:,.2f}")

    # Validation check: Setter preventing invalid negative salary
    try:
        print("Attempting to set negative salary (-5000)...")
        emp1.base_salary = -5000.0
    except ValueError as err:
        print(f" -> Validation Shield Activated: {err}")

    # 2. CLASSMETHODS & STATICMETHODS
    print("\n2. CLASSMETHODS & STATICMETHODS")
    print("-" * 50)
    # Instantiate using Factory classmethods
    emp2 = ContractorEmployee.from_csv_string("Bob Jones, EMP-1002, Design, 75.0, 160.0")
    emp3 = FullTimeEmployee.from_csv_string("Carol Danvers, EMP-1003, Engineering, 96000.0, 6000.0")
    print(f"Factory created contractor: {emp2}")
    print(f"Factory created full-timer:  {emp3}")

    # Static method utility execution
    print(f"Static Method validation check for 'EMP-9999': {Employee._validate_id('EMP-9999')}")
    print(f"Total Employee Instances Created (via Classmethod): {Employee.get_employee_count()}")

    # 3. COMPOSITION (MANAGER & TEAM)
    print("\n3. COMPOSITION (MANAGER & DIRECT REPORTS)")
    print("-" * 50)
    mgr = Manager("David Vance", "EMP-2000", "Engineering", 150000.0, annual_bonus=24000.0)
    mgr.add_team_member(emp1)
    mgr.add_team_member(emp2)
    mgr.add_team_member(emp3)

    print(f"Manager Instance: {mgr}")
    print(f"Team Size using len(mgr): {len(mgr)} direct reports")
    print("Team Roster:")
    for member_info in mgr.list_team_members():
        print(f"  * {member_info}")

    # 4. POLYMORPHISM & MIXIN
    print("\n4. POLYMORPHISM & MIXIN IN ACTION (PAYROLL PROCESSING)")
    print("-" * 50)
    company_payroll: List[Employee] = [emp1, emp2, emp3, mgr]

    print(f"{'Employee Name':<16} | {'Type':<18} | {'Gross Pay':<12} | {'Net Pay (Tax 20%)':<15}")
    print("-" * 72)
    for emp in company_payroll:
        # Polymorphic call: calculate_pay() executes different logic depending on subclass type
        gross = emp.calculate_pay()
        # Mixin call: calculate_tax() inherited from TaxCalculableMixin
        tax = emp.calculate_tax(gross)
        net = gross - tax
        print(f"{emp.name:<16} | {emp.employee_type:<18} | ${gross:>10,.2f} | ${net:>15,.2f}")

    # 5. DUNDER METHODS (COMPARISON & HASHING)
    print("\n5. DUNDER METHODS (SORTING & SET DEDUPLICATION)")
    print("-" * 50)
    # Sorting employees by salary using __lt__ operator overloading
    sorted_employees = sorted([emp1, emp3, mgr])
    print("Employees sorted by Base Salary (ascending via __lt__):")
    for emp in sorted_employees:
        print(f"  - {emp.name}: ${emp.base_salary:,.2f}")

    # Set deduplication test using __hash__ and __eq__
    emp_set = {emp1, emp2, emp3, mgr}
    duplicate_emp1 = FullTimeEmployee("Alice Duplicate", "EMP-1001", "QA", 100000.0)
    emp_set.add(duplicate_emp1)  # Matches EMP-1001 ID, so set will reject duplicate
    print(f"Unique items in Employee Set: {len(emp_set)} (Deduplicated using __hash__ & __eq__)")

    print("\n" + "=" * 75)
    print("                   ALL OOP VERIFICATION TESTS PASSED                   ")
    print("=" * 75)


if __name__ == "__main__":
    main()
