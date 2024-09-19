
```python
# Read a file line by line
def readLine():
    # Open the file in read mode
    file = open("UserModel.py")  # Open the file
    for line in file:  # Iterate over each line in the file
        print(line, end=' ')  # Print each line, with no extra newline
    file.close()  # Close the file to free up resources

readLine()
```

### Explanation:
- **`file = open("UserModel.py")`**: Opens the file `UserModel.py` in read mode.
- **`for line in file:`**: Iterates over each line in the file.
- **`print(line, end=' ')`**: Prints each line. The `end=' '` argument prevents adding an additional newline character after each line (since each line already contains a newline character).
- **`file.close()`**: Closes the file to free up system resources.

Ensure that `UserModel.py` exists in the same directory as your script or provide the correct path to the file.
