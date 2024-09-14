Certainly! Here's the code with comments added, followed by a brief explanation:

```python
# Example of Creating Modules 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Import the specific function 'summation' from the 'Calculations' module
from Calculations import summation    

# Prompt the user to enter the first number
a = int(input("Enter the first number: "))  

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))  

# Calculate the sum of the two numbers using the imported 'summation' function
print("Sum = ", summation(a, b))  # No need to specify the module name here
```

### Brief Explanation:

1. **Import Statement**:
   - **`from Calculations import summation`**:
     - This line imports only the `summation` function from the `Calculations` module. This means you can use `summation` directly without prefixing it with the module name.

2. **User Input**:
   - **`a = int(input("Enter the first number: "))`**:
     - Prompts the user to enter the first number and converts the input to an integer.
   - **`b = int(input("Enter the second number: "))`**:
     - Prompts the user to enter the second number and converts the input to an integer.

3. **Function Call**:
   - **`print("Sum = ", summation(a, b))`**:
     - Calls the `summation` function (imported from the `Calculations` module) with the user-provided numbers and prints the result. Since `summation` is imported directly, there's no need to specify the module name.

### Summary:
- This code demonstrates how to import specific functions from a module.
- It collects user input for two numbers, computes their sum using the imported function, and then prints the result.