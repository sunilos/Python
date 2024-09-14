Here’s the code with added comments and a brief explanation:

```python
# Example of If-else control statement
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Variable to store the price of an item
price = 99  # Let's assume the price of an item (in this case, pizza) is 99

# If-else control structure to check if the price is less than 100
if price < 100:
    # This block executes if the condition is true (price is less than 100)
    print("I can not buy Pizza")  # Output message indicating that pizza can't be bought
    print("Feeling bad :(")  # A sad expression
else:
    # This block executes if the condition is false (price is 100 or more)
    print("I can buy Pizza")  # Output message indicating that pizza can be bought
    print("Yu Yum :)")  # A happy expression
```

### Explanation:

1. **Variable Initialization**:
   - `price = 99`: The price of an item (pizza) is stored in the variable `price`.

2. **If-Else Statement**:
   - **Condition**: The `if` condition checks if the `price` is less than 100 (`if price < 100:`).
   - If the condition is true (i.e., the price is below 100), it executes the code in the `if` block:
     - Prints "I can not buy Pizza" and "Feeling bad :(" to express disappointment.
   - If the condition is false (i.e., the price is 100 or more), it jumps to the `else` block:
     - Prints "I can buy Pizza" and "Yu Yum :)" to express happiness.

3. **Output**:
   - Since `price = 99` (which is less than 100), the program will execute the `if` block and print:
     ```
     I can not buy Pizza
     Feeling bad :(
     ```

This simple program demonstrates how conditional control flow (if-else) works, making decisions based on a condition.