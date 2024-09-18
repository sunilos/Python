Here's the code snippet for file I/O that prints the properties of a file:

```python
# Example of File I/O
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Prints properties of a file
def fileInfo():
    fo = open("Test.py", "wb") 
    print("File Name: ", fo.name)
    print("Mode of Opening: ", fo.mode)
    print("Is Closed: ", fo.closed)
    
fileInfo()
```

### Explanation:
- **`def fileInfo()`**: Defines a function named `fileInfo` that performs file operations.

- **`fo = open("Test.py", "wb")`**: Opens the file `Test.py` in binary write mode (`"wb"`). If the file does not exist, it will be created. If it already exists, it will be truncated.

- **`fo.name`**: Returns the name of the file.

- **`fo.mode`**: Returns the mode in which the file was opened.

- **`fo.closed`**: Returns `False` because the file is still open at this point.

- **`fileInfo()`**: Calls the `fileInfo` function to execute the file operations and print the properties.
