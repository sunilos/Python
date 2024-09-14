Here’s the code with added comments and a brief explanation:

```python
# Example of Array List to delete Existing Element
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

from array import array  # Import the 'array' class from the 'array' module

# Initialize an array with integer type ('i') and some elements
array_list = array('i', [10, 20, 30, 40, 50])

# Remove the element 30 from the array
array_list.remove(30)

# Iterate over the array and print each element
for x in array_list:
    print(x)  # Output: remaining elements in the array
```

### Explanation:

1. **Importing `array`**:
   - The `array` class from the `array` module is imported to work with arrays in Python.

2. **Creating an Array**:
   - `array('i', [10, 20, 30, 40, 50])`: Initializes an array named `array_list` with integer type (`'i'`) and populates it with the elements `[10, 20, 30, 40, 50]`.

3. **Removing an Element**:
   - `array_list.remove(30)`: Removes the first occurrence of the element `30` from the array.

4. **Iterating and Printing**:
   - The `for` loop iterates over the elements of the array and prints each element.

5. **Output**:
   - After removing `30`, the array will contain `[10, 20, 40, 50]`.
   - The program will output:
     ```
     10
     20
     40
     50
     ```

This code demonstrates how to create an array, remove an element from it, and then print the remaining elements.