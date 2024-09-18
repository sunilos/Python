Here's the code that demonstrates exception handling with a `finally` clause:

```python
# Example of Exception Handling with Finally() Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

def hello():
    try:
        return 1
    finally:
        return 2

k = hello()
print(k)  # The finally block is executed even if there is a return statement in the try block.
```

### Explanation:
- **`try` block**:
  - Contains a `return` statement that attempts to return the value `1`.

- **`finally` block**:
  - Executes after the `try` block, regardless of whether an exception was raised or not.
  - Contains a `return` statement that attempts to return the value `2`.

- **Result**:
  - The `finally` block overrides the `return` value from the `try` block, so the function `hello()` returns `2`.

The `finally` block is always executed, which can be useful for cleanup operations or to ensure certain code runs regardless of the outcome of the `try` block.
