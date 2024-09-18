Here’s the code with comments and a brief explanation:

```python
# Example of Operators
# Example of Identity Operator
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Initialize lists
x = ["apple", "banana"]  # List x containing two elements
y = ["apple", "banana"]  # List y containing the same elements as x
z = x                   # z is assigned the same reference as x

# Identity operator checks
print(x is z)  # Checks if x and z refer to the same object in memory
# Output will be True because z is assigned to x

print(x is y)  # Checks if x and y refer to the same object in memory
# Output will be False because x and y are two different objects with the same content

print(x == y)  # Checks if the contents of x and y are the same
# Output will be True because x and y have the same elements
```

### Explanation:

1. **Identity Operator (`is`)**:
   - `x is z`: This checks if `x` and `z` refer to the same object in memory. Since `z` is assigned to `x`, they refer to the same object, so the result is `True`.
   - `x is y`: This checks if `x` and `y` refer to the same object in memory. Even though `x` and `y` have the same contents, they are two distinct objects, so the result is `False`.

2. **Equality Operator (`==`)**:
   - `x == y`: This checks if the contents of `x` and `y` are the same. Since both lists have the same elements, the result is `True`.

Identity operators (`is` and `is not`) compare the memory locations of objects, while equality operators (`==` and `!=`) compare the values of objects.
