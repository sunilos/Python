Here's the code that demonstrates handling a `ValueError` in a `try` block with a `while` loop:

```python
# Example of Try Except with ValueError  
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

while True:  
    try:
        x = int(input("Please enter a number: "))
        print("%s squared is %s" % (x, x**5))
    except ValueError:
        print("Please enter a valid number!")
```

### Explanation:
- **`while True:`**: This creates an infinite loop, allowing the user to repeatedly enter numbers until they provide valid input or the program is terminated.

- **`try` block**:
  - Attempts to convert user input to an integer.
  - If successful, it prints the result of raising the number to the power of 5.

- **`except ValueError`**:
  - Catches the exception if the user input cannot be converted to an integer (e.g., if the user inputs non-numeric text).
  - Prints an error message prompting the user to enter a valid number.

The loop will continue indefinitely, prompting the user to enter a number until valid input is provided.