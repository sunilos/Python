Here’s the code with added comments and a brief explanation:

```python
# Example of Update Element in Array List
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Array Updation
from array import array  # Import the 'array' class from the 'array' module

# Initialize an array with integer type ('i') and some elements
arraylist = array('i', [10, 20, 30, 40, 50])

# Update the element at index 2 to 80
arraylist[2] = 80

# Iterate over the array and print each element
for x in arraylist:
    print(x)  # Output: updated elements of the array
```

### Explanation:

1. **Importing `array`**:
   - The `array` class from the `array` module is imported to work with arrays.

2. **Creating an Array**:
   - `array('i', [10, 20, 30, 40, 50])`: Initializes an array named `arraylist` with integer type (`'i'`) and populates it with the elements `[10, 20, 30, 40, 50]`.

3. **Updating an Element**:
   - `arraylist[2] = 80`: Updates the element at index `2` of the array to `80`. The array is modified from `[10, 20, 30, 40, 50]` to `[10, 20, 80, 40, 50]`.

4. **Iterating and Printing**:
   - The `for` loop iterates over the elements of the array and prints each element.

5. **Output**:
   - After updating the element at index `2`, the array will contain `[10, 20, 80, 40, 50]`.
   - The program will output:
     ```
     10
     20
     80
     40
     50
     ```

This code demonstrates how to update an element in an array and then print the updated array.
