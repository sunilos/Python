Here's the code with additional comments and a brief explanation:

```python
# Example of Creating Modules 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Import only the 'summation' function from the 'Calculations' module
from Calculations import summation    

# Prompt the user to enter the first number
a = int(input("Enter the first number "))  

# Prompt the user to enter the second number
b = int(input("Enter the second number "))  

# Call the 'summation' function with the input values and print the result
print("Sum = ", summation(a, b))  # We do not need to specify the module name while accessing summation()
```

### Brief Explanation:

1. **Import Statement**: 
   - `from Calculations import summation` imports only the `summation` function from the `Calculations` module, allowing us to use it directly without prefixing it with the module name.

2. **User Input**:
   - `a = int(input("Enter the first number "))` prompts the user to enter a number and converts it to an integer.
   - `b = int(input("Enter the second number "))` does the same for the second number.

3. **Function Call**:
   - `print("Sum = ", summation(a, b))` calls the `summation` function with the two user-provided numbers as arguments and prints the result. The `summation` function calculates and returns the sum of the two numbers.