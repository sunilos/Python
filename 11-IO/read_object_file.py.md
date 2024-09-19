
```python
# Example of deserialization of an object from a file.
# Pickle library is used for serialization and deserialization 

import pickle

with open('emp.dat', 'rb') as f:
    obj = pickle.load(f)  # Deserialize the object from the file
    print("Printing Employee information after unpickling")
    obj.display()  # Assuming 'obj' has a 'display' method
```

### Explanation:
- **`import pickle`**: Imports the `pickle` library which is used for serializing (pickling) and deserializing (unpickling) Python objects.
- **`with open('emp.dat', 'rb') as f:`**: Opens the file `emp.dat` in binary read mode (`'rb'`). Using `with` ensures the file is properly closed after the block of code is executed.
- **`obj = pickle.load(f)`**: Reads (unpickles) the object from the file and assigns it to `obj`.
- **`obj.display()`**: Calls the `display` method on the deserialized object, assuming that the object has such a method. This is where you would handle the deserialized object's data.

