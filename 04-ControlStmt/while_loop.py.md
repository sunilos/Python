Here’s the code with added comments and a brief explanation:

```python
# Example of While Loop
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Initialize a variable i with value 0
i = 0

# While loop: repeat as long as the value of i is less than 5
while i < 5:
    # Print a message and the current value of i
    print('Hello', i)
    
    # Increment i by 1 to avoid an infinite loop
    i += 1
```

### Explanation:

1. **Variable Initialization**:
   - The variable `i` is initialized with the value `0`.

2. **While Loop**:
   - The loop runs while the condition `i < 5` is true. Each iteration of the loop will check the value of `i`.
   - Inside the loop:
     - The program prints the message `"Hello"` followed by the current value of `i`.
     - After printing, `i` is incremented by `1` using `i += 1`.
   - The loop will continue until `i` reaches 5, at which point the condition `i < 5` becomes false, and the loop exits.

3. **Output**:
   - The program will print the following output:
     ```
     Hello 0
     Hello 1
     Hello 2
     Hello 3
     Hello 4
     ```

This simple program demonstrates how a `while` loop works, repeating an action while a certain condition (in this case, `i < 5`) is true. Each iteration updates the loop variable (`i`), preventing infinite loops.
