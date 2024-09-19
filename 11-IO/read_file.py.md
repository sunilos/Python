
```python
# Read a file 
def readFile():
    file = open("FileInfo.py")  # Open the file named "FileInfo.py" in read mode
    text = file.read()  # Read the entire content of the file
    print(text)  # Print the content of the file
    file.close()  # Close the file to release resources

readFile()
```

### Explanation:
- **`def readFile():`**: Defines a function `readFile` to encapsulate the file reading operations.
- **`file = open("FileInfo.py")`**: Opens the file `FileInfo.py` in read mode. If the file does not exist, it will raise an error.
- **`text = file.read()`**: Reads all the data from the file and stores it in the variable `text`.
- **`print(text)`**: Outputs the contents of the file to the console.
- **`file.close()`**: Closes the file to ensure resources are properly released.

