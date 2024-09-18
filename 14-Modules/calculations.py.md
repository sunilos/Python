```python
# Example of Defining Calculation Modules 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Defining a function for summation of two numbers
def summation(a, b):  
    # Returns the sum of a and b
    return a + b  

# Defining a function for multiplication of two numbers
def multiplication(a, b):  
    # Returns the product of a and b
    return a * b  

# Defining a function for division of two numbers
def divide(a, b):  
    # Returns the result of dividing a by b
    return a / b
```

### Explanation:

1. **Module Overview**:
   - This module defines three simple mathematical functions: summation, multiplication, and division.

2. **Function `summation(a, b)`**:
   - Takes two arguments, `a` and `b`.
   - Returns the sum of `a` and `b` using the `+` operator.

3. **Function `multiplication(a, b)`**:
   - Takes two arguments, `a` and `b`.
   - Returns the product of `a` and `b` using the `*` operator.

4. **Function `divide(a, b)`**:
   - Takes two arguments, `a` and `b`.
   - Returns the result of dividing `a` by `b` using the `/` operator.

### Usage Example:

```python
# Example usage:
x = 10
y = 5

print(summation(x, y))  # Output: 15
print(multiplication(x, y))  # Output: 50
print(divide(x, y))  # Output: 2.0
```

This code demonstrates basic mathematical operations and can be reused in different Python programs or imported as a module for calculations.
