
```python
# Example of Encapsulation
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

class Person:
    def __init__(self):
        """
        Constructor to initialize the Person object.
        """
        # Instance variable
        self.name = "No name"

    def display(self, name):
        """
        Method to display a greeting with the provided name.
        """
        print("Hello", name)

# Create an instance of the Person class
obj = Person()

# Call the display method with different names
obj.display("Ram")   # Output: Hello Ram
obj.display("Shyam") # Output: Hello Shyam
```

### Explanation:

1. **Class Definition**:
   - `class Person:`: Defines a class named `Person`.

2. **Constructor (`__init__` method)**:
   - `def __init__(self):`: Defines the constructor method that initializes a new instance of the `Person` class.
   - `self.name = "No name"`: Initializes the instance variable `name` with the default value `"No name"`. This is a simple example of encapsulation, as the `name` attribute is internal to the class and can be set or modified through methods.

3. **Method**:
   - `def display(self, name):`: Defines a method `display` that takes an additional parameter `name` and prints a greeting message.
   - `print("Hello", name)`: Prints the greeting message using the provided `name`.

4. **Creating an Instance**:
   - `obj = Person()`: Creates an instance of the `Person` class. The `name` attribute is initialized to `"No name"`.

5. **Calling Method**:
   - `obj.display("Ram")`: Calls the `display` method with the argument `"Ram"`, printing `Hello Ram`.
   - `obj.display("Shyam")`: Calls the `display` method with the argument `"Shyam"`, printing `Hello Shyam`.

