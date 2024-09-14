Here’s the code with comments and a brief explanation:

```python
# Example of Logical Operator
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Initialize boolean variables
x = True   # Boolean value True
y = False  # Boolean value False

# Logical AND
print("X and Y =", x and y)  
# Output will be False because x is True and y is False; AND operation requires both to be True.

# Logical OR
print("X or Y =", x or y)   
# Output will be True because x is True; OR operation requires at least one to be True.

# Logical NOT
print("Not of X =", not x)  
# Output will be False because x is True; NOT operation inverts the value.
```

### Explanation:

1. **Logical AND (`and`)**:
   - `x and y`: This evaluates to `True` only if both `x` and `y` are `True`. Since `y` is `False`, the result is `False`.

2. **Logical OR (`or`)**:
   - `x or y`: This evaluates to `True` if at least one of `x` or `y` is `True`. Since `x` is `True`, the result is `True`.

3. **Logical NOT (`not`)**:
   - `not x`: This inverts the value of `x`. Since `x` is `True`, `not x` results in `False`.

Logical operators are used to combine or invert boolean values in conditional statements and expressions.