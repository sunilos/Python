Here’s the code with added comments and a brief explanation:

```python
# Example of Simple Array to print Index Values
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

from array import array  # Import the 'array' class from the 'array' module

# Initialize an array with integer type ('i') and some elements
array_list = array('i', [10, 20, 30, 40, 50])

# Print the element at index 0
print(array_list[0])  # Output: 10

# Print the element at index 2
print(array_list[2])  # Output: 30
```

### Explanation:

1. **Importing `array`**:
   - The `array` class from the `array` module is imported to work with arrays.

2. **Creating an Array**:
   - `array('i', [10, 20, 30, 40, 50])`: Initializes an array named `array_list` with integer type (`'i'`) and populates it with the elements `[10, 20, 30, 40, 50]`.

3. **Printing Elements**:
   - `print(array_list[0])`: Prints the element at index `0` of the array, which is `10`.
   - `print(array_list[2])`: Prints the element at index `2` of the array, which is `30`.

4. **Output**:
   - The program will output:
     ```
     10
     30
     ```

This code demonstrates how to access and print specific elements from an array based on their index positions.