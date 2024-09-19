
```python
# Example of simple Try Except with NameError
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

# The try block will generate a NameError, because `name` is not defined:
try:
    print(name)
except NameError:
    print("Variable name is not defined")
except:
    print("Something else went wrong")
```

### Explanation:
- **`try` Block**:
  - Contains the code that might raise an exception. In this case, trying to print `name` will raise a `NameError` because `name` is not defined.

- **`except NameError` Block**:
  - Catches the `NameError` and prints a specific message indicating that the variable `name` is not defined.

- **`except` Block**:
  - Catches any other exceptions that are not specifically handled by the previous `except` blocks and prints a generic error message.

