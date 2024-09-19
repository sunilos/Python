
```python
# Example of Multiple Inheritance
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

class Addition:
    def sum(self, a, b):
        """
        Method to return the sum of two numbers.
        """
        return a + b

class Multiplication:
    def multiply(self, a, b):
        """
        Method to return the product of two numbers.
        """
        return a * b

class Derived(Addition, Multiplication):  # Derived class inherits both Addition and Multiplication base classes
    def Divide(self, a, b):
        """
        Method to return the division of two numbers.
        """
        return a / b

# Create an instance of the Derived class
derived_obj = Derived()
# Call methods from the Addition and Multiplication classes and the Derived class
print(derived_obj.sum(10, 20))        # Output: 30
print(derived_obj.multiply(10, 20))   # Output: 200
print(derived_obj.Divide(10, 20))     # Output: 0.5
```

### Explanation:

1. **Base Classes**:
   - **`Addition`**: Contains a method `sum()` that returns the sum of two numbers.
   - **`Multiplication`**: Contains a method `multiply()` that returns the product of two numbers.

2. **Derived Class (`Derived`)**:
   - Inherits from both `Addition` and `Multiplication`.
   - Adds a new method `Divide()` that returns the result of dividing two numbers.

3. **Multiple Inheritance**:
   - `Derived` class inherits methods from both `Addition` and `Multiplication`.
   - This allows `Derived` to use methods from both parent classes in addition to its own methods.

### Key Points:
- **Multiple Inheritance**: A class can inherit from more than one base class, combining their functionalities.
- **Method Access**: The `Derived` class can call methods `sum()` and `multiply()` from the base classes `Addition` and `Multiplication`, respectively, and also use its own `Divide()` method.

This example demonstrates how multiple inheritance allows combining features from multiple base classes into a single derived class.
