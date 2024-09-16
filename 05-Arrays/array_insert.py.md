Here’s the code with added comments and a brief explanation:

```python
# Example of Array to Insert Element using Index
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

from array import array  # Import the 'array' class from the 'array' module

# Initialize an array with integer type ('i') and some elements
array_list = array('i', [10, 20, 30, 40, 50])

# Insert the element 60 at index 1 in the array
array_list.insert(1, 60)

# Iterate over the array and print each element
for x in array_list:
    print(x)  # Output: elements of the array after insertion
```

### Explanation:

1. **Importing `array`**:
   - The `array` class from the `array` module is imported to work with arrays.

2. **Creating an Array**:
   - `array('i', [10, 20, 30, 40, 50])`: Initializes an array named `array_list` with integer type (`'i'`) and populates it with the elements `[10, 20, 30, 40, 50]`.

3. **Inserting an Element**:
   - `array_list.insert(1, 60)`: Inserts the element `60` at index `1` in the array. The array will now be `[10, 60, 20, 30, 40, 50]`.

4. **Iterating and Printing**:
   - The `for` loop iterates over the elements of the array and prints each element.

5. **Output**:
   - After inserting `60` at index `1`, the array will contain `[10, 60, 20, 30, 40, 50]`.
   - The program will output:
     ```
     10
     60
     20
     30
     40
     50
     ```

This code demonstrates how to insert an element into an array at a specific index and print the updated array.
