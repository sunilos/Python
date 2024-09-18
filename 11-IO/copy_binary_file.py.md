Here's the code snippet for copying a binary file using Python's `shutil` module:

```python
# Copy a Binary File
import shutil

source = "F:/baby.jpg"
target = "F:/boy.jpg"

shutil.copyfile(source, target)
print(source + " is copied to " + target)
```

### Explanation:
- **`import shutil`**: Imports the `shutil` module, which provides a range of file operations including copying files.

- **`source` and `target`**: Define the paths for the source file and the target file where the copy will be saved.

- **`shutil.copyfile(source, target)`**: Copies the contents of the source file to the target file. If the target file already exists, it will be overwritten.

- **`print(source + " is copied to " + target)`**: Prints a confirmation message indicating that the file copy operation has been completed.
