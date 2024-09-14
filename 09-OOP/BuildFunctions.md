Here's the code with added comments and a brief explanation:

```python
# Example of Built-in Class Attributes
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

class Student:  
    'Document of this class'
    
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
    
    def display_details(self):  
        """
        Print the details of the student.
        """
        print("Name: %s, ID: %d, Age: %d" % (self.name, self.id, self.age))  

# Create an instance of the Student class
s = Student("John", 101, 22)  

# Accessing built-in class attributes
print(Student.__doc__)   # Prints the documentation string of the class, if available. Otherwise, it returns None.
print(Student.__name__)  # Prints the name of the class.
print(s.__dict__)        # Prints the __dict__ attribute of the instance, which is a dictionary containing the instance's namespace.
print(s.__module__)      # Prints the name of the module in which the class is defined.
```

### Explanation:

1. **Class Definition**:
   - `class Student`: Defines a class named `Student`.
   - `def __init__(self, name, id, age)`: The constructor method initializes the instance with `name`, `id`, and `age`.

2. **Method**:
   - `def display_details(self)`: A method that prints the student's details.

3. **Built-in Class Attributes**:
   - `Student.__doc__`: Retrieves the documentation string (docstring) for the class. This is useful for providing a description or documentation of what the class does.
   - `Student.__name__`: Returns the name of the class as a string. For this example, it will print `"Student"`.
   - `s.__dict__`: Returns a dictionary representation of the instance's attributes and their values. For the instance `s`, this will show `{'name': 'John', 'id': 101, 'age': 22}`.
   - `s.__module__`: Returns the name of the module in which the class is defined. This is useful for understanding where the class is located in a larger codebase.

These built-in attributes provide useful metadata and introspection capabilities about classes and their instances in Python.