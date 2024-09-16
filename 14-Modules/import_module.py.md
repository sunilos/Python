```python
# Example of Creating Modules 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Importing the summation function from the Calculations module
from Calculations import summation    

# This imports only the summation() function from the file 'calculation.py' located in the 'Calculations' module

# Taking two input numbers from the user
a = int(input("Enter the first number "))  # Converts the input string into an integer
b = int(input("Enter the second number "))  # Converts the input string into an integer

# Calling the summation() function and printing the result
print("Sum = ", summation(a, b))  
# Here, we call the summation() function directly without needing to specify the module name
```

### Explanation:

1. **Creating and Using Modules**:
   - This example demonstrates how to create and use a module in Python.
   - A module in Python is a file that contains functions, classes, or variables which can be reused in different programs by importing them.

2. **Import Statement**:
   - `from Calculations import summation`: This line imports the `summation()` function from the `Calculations` module (a file named `calculation.py`).
   - By importing only the specific function, you can use `summation()` directly in your code without needing to prefix it with the module name (e.g., `Calculations.summation()`).

3. **Input from User**:
   - `input()` prompts the user to enter a number. The `int()` function is used to convert the string input into an integer for performing arithmetic operations.

4. **Calling the Function**:
   - After taking inputs `a` and `b` from the user, the `summation(a, b)` function is called to add the two numbers.
   - The result is printed using `print()` in the format `Sum = result`.

### Assumptions:
- The `Calculations` module (file named `calculation.py`) contains a function `summation()` which adds two numbers.
- The structure would look like this:
   ```
   Calculations/
       └── calculation.py
   ```

### Example Usage:

If you run this program and input numbers 5 and 10:
```bash
Enter the first number 5
Enter the second number 10
Sum = 15
```
