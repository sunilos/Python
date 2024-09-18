
```python
# Example of simple Try Except with ZeroDivisionError
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

try:  
    num1 = int(input("Enter First Number: "))  
    num2 = int(input("Enter Second Number: "))  
    num3 = num1 / num2;  
    print("num1 / num2 = ", num3)  
except ZeroDivisionError:  
    print("Can't divide by zero")  
else:  
    print("Hi, I am the else block")
```

### Explanation:
- **`try` block**:
  - Prompts the user for two numbers and attempts to divide them.
  - If the second number is zero, a `ZeroDivisionError` is raised.

- **`except ZeroDivisionError` block**:
  - Catches the `ZeroDivisionError` and prints an error message.

- **`else` block**:
  - Executes if no exception is raised in the `try` block. It prints a message indicating the `else` block was executed.

