Here’s the code with added comments and a brief explanation:

```python
# Example of For Loop to print squares of all numbers present in a list
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# List of integer numbers
numbers = [1, 2, 4, 6, 11, 20]  # A list containing several integer values

# Iterating over the given list using a for loop
for val in numbers:  
    # Calculating the square of each number in the list
    square = val * val  
    # Displaying the square of the current number
    print(square)  # Output: square of the current number
```

### Explanation:

1. **List of Numbers**:
   - A list named `numbers` is created, containing a set of integers: `[1, 2, 4, 6, 11, 20]`.

2. **For Loop**:
   - The `for` loop is used to iterate over the list. In each iteration, the variable `val` takes the value of each number from the list one by one.

3. **Square Calculation**:
   - Inside the loop, the square of each number is calculated by multiplying the number with itself: `square = val * val`.

4. **Printing the Squares**:
   - After calculating the square of the number, the result is printed. For example, the square of 2 is `4`, and it will be printed to the console.

This program will output the squares of all the numbers present in the list one by one.