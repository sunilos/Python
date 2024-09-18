
```python
# Example of Membership Operator
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Initialize variables
a = 10          # Value to check in the list
b = 20          # Another value to check in the list
list = [1, 2, 3, 4, 5]  # List to check membership against

# Check if 'a' is in the list
if a in list:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

# Check if 'b' is not in the list
if b not in list:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

# Update 'a' and check if 'a' is in the list
a = 2
if a in list:
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")
```

### Explanation:

1. **Membership Operator (`in`)**:
   - `a in list`: Checks if the value of `a` (initially 10) is present in `list`. Since 10 is not in `[1, 2, 3, 4, 5]`, it prints `"Line 1 - a is not available in the given list"`.

2. **Membership Operator (`not in`)**:
   - `b not in list`: Checks if the value of `b` (20) is not present in `list`. Since 20 is not in `[1, 2, 3, 4, 5]`, it prints `"Line 2 - b is not available in the given list"`.

3. **Update and Check Membership**:
   - `a` is updated to 2, and `a in list` is checked again. Since 2 is present in `[1, 2, 3, 4, 5]`, it prints `"Line 3 - a is available in the given list"`.

Membership operators check for the presence or absence of a value in a sequence like lists, tuples, or strings.
