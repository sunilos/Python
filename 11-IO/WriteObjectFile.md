Here's the code for serializing an object into a file using the `pickle` library:

```python
# Example of serialization of an object into a file.
# Pickle library is used for serialization and deserialization 

import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)

# Create an instance of Employee
e = Employee(1, 'Mayank', 1000, 'Indore')

# Serialize the object to a file
with open('emp.dat', 'wb') as f:
    pickle.dump(e, f)
    print("Pickling of Employee Object completed")
```

### Explanation:
- **`import pickle`**: Imports the `pickle` library, which is used for serializing and deserializing Python objects.
- **`class Employee:`**: Defines the `Employee` class with an `__init__` method to initialize attributes and a `display` method to print the employee details.
- **`e = Employee(1, 'Mayank', 1000, 'Indore')`**: Creates an instance of the `Employee` class with specified attributes.
- **`with open('emp.dat', 'wb') as f:`**: Opens the file `emp.dat` in write-binary mode (`'wb'`).
- **`pickle.dump(e, f)`**: Serializes the `Employee` object `e` and writes it to the file `emp.dat`.
- **`print("Pickling of Employee Object completed")`**: Prints a confirmation message after serialization is complete.