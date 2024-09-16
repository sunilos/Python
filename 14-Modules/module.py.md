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
# This will import only the summation() function from the 'calculation.py' file inside the 'Calculations' module

# Taking two input numbers from the user
a = int(input("Enter the first number "))  
# The input function takes user input as a string, and int() converts it into an integer

b = int(input("Enter the second number "))  
# Similarly, the second input is also converted into an integer

# Calling the summation() function with the two inputs
print("Sum = ", summation(a, b))  
# summation(a, b) calculates the sum of the two numbers and returns the result
# We print the result using the print() function
# No need to specify the module name (Calculations) since summation() was directly imported
```

### Explanation:

1. **Import Statement**:
   - `from Calculations import summation`: This imports only the `summation()` function from the `Calculations` module (which is a separate file, likely named `calculation.py`).
   - This allows us to call `summation()` directly without prefixing it with `Calculations`.

2. **User Input**:
   - The user is prompted to input two numbers using `input()`. Since `input()` returns the value as a string, we use `int()` to convert the input into integers for the summation function.

3. **Function Call**:
   - `summation(a, b)` adds the two numbers `a` and `b` and returns the result.
   - The `print()` function then prints the result in the format: `Sum = result`.

### Practical Usage:
- This example shows how to import specific functions from a module and use them without needing to reference the module name every time.
- The module should be structured like:
  ```
  Calculations/
      └── calculation.py  # contains the summation() function
  ```

### Example:

When the user runs this script and inputs:
```bash
Enter the first number 5
Enter the second number 10
Sum = 15
```

This shows the result of the summation function as `15`.
