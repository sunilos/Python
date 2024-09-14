Here’s the code with added comments and a brief explanation:

```python
# Example of Number to find out their types
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Create a variable with an integer value
a = 10  # Assigning an integer value to 'a'
print("The type of variable having value", a, "is", type(a))  # Output: The type of variable having value 10 is <class 'int'>

# Create a variable with a float value
b = 10.2345  # Assigning a float value to 'b'
print("The type of variable having value", b, "is", type(b))  # Output: The type of variable having value 10.2345 is <class 'float'>

# Create a variable with a complex value
c = 100 + 3j  # Assigning a complex number to 'c'
print("The type of variable having value", c, "is", type(c))  # Output: The type of variable having value (100+3j) is <class 'complex'>
```

### Explanation:

1. **Integer Type**: 
   - The variable `a` is assigned an integer value `10`. The `type(a)` function checks the type of `a`, which is `<class 'int'>`.

2. **Float Type**: 
   - The variable `b` is assigned a floating-point value `10.2345`. The `type(b)` function checks the type of `b`, which is `<class 'float'>`.

3. **Complex Type**: 
   - The variable `c` is assigned a complex number `100 + 3j` (where `j` represents the imaginary unit). The `type(c)` function checks the type of `c`, which is `<class 'complex'>`.

4. **Output**: 
   - The `print()` statements display the value of each variable along with its type (`int`, `float`, `complex`).