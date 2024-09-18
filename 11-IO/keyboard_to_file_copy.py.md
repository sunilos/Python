
```python
# Reads text from keyboard and stores it into a text file. 

def KeyboardToFileCopy():
    # Open a file for writing
    file = open("Test.txt", "w") 
    print('Enter your message (type "quit" to stop):')
    
    while True:
        text = input()
        if text == "quit":
            break
        file.write(text)
        file.write(" ")
    
    file.close() # Close the file

KeyboardToFileCopy()
```

### Explanation:
- **`def KeyboardToFileCopy()`**: Defines a function named `KeyboardToFileCopy` to handle reading from the keyboard and writing to a file.

- **`file = open("Test.txt", "w")`**: Opens (or creates) a file named `Test.txt` in write mode (`"w"`). If the file already exists, its contents will be overwritten.

- **`print('Enter your message (type "quit" to stop):')`**: Prompts the user to enter text.

- **`while True:`**: Starts an infinite loop that continues until `break` is executed.

- **`text = input()`**: Reads a line of input from the user.

- **`if text == "quit":`**: Checks if the input is `"quit"`. If so, it breaks out of the loop.

- **`file.write(text)`**: Writes the input text to the file.

- **`file.write(" ")`**: Adds a space after each line of text for separation.

- **`file.close()`**: Closes the file after all input has been written.

- **`KeyboardToFileCopy()`**: Calls the function to execute the operations.
