Here’s the code for raising an exception if a condition is met:

```python
# Example of Simple Raising Exception
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

number = int(input("Enter your Number: "))
if number > 10:
    raise Exception('x should not exceed 10. The value of number was: {}'.format(number))
```

### Explanation:
- **`number = int(input("Enter your Number: "))`**:
  - Prompts the user to input a number and converts it to an integer.

- **`if number > 10:`**:
  - Checks if the input number exceeds 10.

- **`raise Exception(...)`**:
  - Raises an `Exception` with a custom error message if the condition is true.
  - The message includes the value of `number` that caused the exception to be raised.

This example shows how to manually trigger an exception in Python to enforce constraints or validate input.