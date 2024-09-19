
```python
# Read all text from a file
def readFile():
    file = open("abc.txt")  # Open the file in read mode (default is 'r')
    text = file.read()  # Read all data from the file
    print(text)  # Print the content of the file
    file.close()  # Close the file

readFile()
```

### Explanation:
- **`file = open("abc.txt")`**: Opens the file `abc.txt` in read mode. If the file does not exist, it will raise an error.
- **`text = file.read()`**: Reads the entire content of the file into the variable `text`.
- **`print(text)`**: Outputs the content of the file to the console.
- **`file.close()`**: Closes the file to free up system resources.

