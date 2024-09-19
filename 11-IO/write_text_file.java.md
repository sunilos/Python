

```python
def writeFile():
    """
    Writes predefined text to a file named 'Test.txt'.
    
    - Opens the file in write mode ('w'), which creates a new file or overwrites an existing one.
    - Writes two lines of text: 'Hi' and 'This is Python file'.
    - Closes the file to ensure the data is saved properly and the file is released.
    """
    # Open the file in write mode
    file = open("Test.txt", "w")
    
    # Write the first line to the file
    file.write("Hi\n")
    
    # Write the second line to the file
    file.write("This is Python file")
    
    # Close the file
    file.close()

writeFile()
```

### Explanation:
- **open("Test.txt", "w")**: Opens the file "Test.txt" in write mode (`"w"`). If the file does not exist, it will be created. If it already exists, its contents will be overwritten.
- **file.write()**: Writes the given string to the file. Each `write()` call writes a line of text.
- **file.close()**: Closes the file, ensuring that all data is written and the file is no longer in use.
