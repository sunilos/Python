```python
# Example of Renaming Calculations Module 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Importing the Calculations module and renaming it as 'cal' for convenience
import Calculations as cal  
# 'Calculations' module is now accessible using the alias 'cal'

# Taking two input numbers from the user
a = int(input("Enter the first number "))  
# The user enters the first number, which is converted from string to integer using int()

b = int(input("Enter the second number "))  
# Similarly, the second input is converted into an integer

# Calling the summation() function from the 'cal' alias
print("Sum = ", cal.summation(a, b))  
# Since we renamed 'Calculations' to 'cal', we use 'cal.summation()' to call the summation function
```

### Explanation:

1. **Module Alias**:
   - `import Calculations as cal`: This line imports the `Calculations` module but renames it as `cal` for simplicity. This allows shorter syntax when accessing functions from the module.

2. **User Input**:
   - The script prompts the user to enter two numbers using the `input()` function, which are then converted to integers using `int()`.

3. **Calling the Function**:
   - After importing the module as `cal`, we use `cal.summation(a, b)` to call the `summation()` function from the `Calculations` module. The result of adding the two numbers is printed.

4. **Renaming Modules**:
   - Renaming modules with an alias (using `as`) is a common practice to shorten module names and make the code easier to read and type.

### Example:

If the user inputs:
```bash
Enter the first number 7
Enter the second number 12
Sum = 19
```

This shows the result of the summation function as `19`.

