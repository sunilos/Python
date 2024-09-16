Here is the provided code snippet for the `Shape` class with an example of inheritance:

```python
# Example of Inheritance 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

class Shape:
   'Shape expert class contains shape related attributes and methods'
   count = 0 # Class variable

   # Define constructor using __init__ method
   def __init__(self, c, b): # Constructor receiving two parameters 
      self.color = c   # Instance variable
      self.borderWidth = b # Instance variable
      Shape.count += 1 # Increase count

   # Define destructor using __del__ method
   def __del__(self):
      className = self.__class__.__name__
      print("Destroying", className)

   # Calculate area of Shape
   def area(self):   
     print("I don't know how to calculate area")
     return -1

   # Print info of Shape
   def info(self):   
     print("Color: %s" % self.color)
     print("Border Width: %s" % self.borderWidth)

   # Define a method to display the count of shapes
   def displayCount(self):
     print("Total Shape %d" % Shape.count)

   def __str__(self):
     return "Shape: Color %s Border Width %i" % (self.color, self.borderWidth)
```

### Explanation:

1. **Class Definition**:
   - **`Shape`**: A base class representing a geometric shape.

2. **Class Variable**:
   - **`count`**: A class variable to keep track of the number of `Shape` objects created.

3. **Constructor (`__init__` method)**:
   - Initializes instance variables `color` and `borderWidth`.
   - Increments the `Shape.count` every time a new `Shape` object is created.

4. **Destructor (`__del__` method)**:
   - Prints a message indicating the destruction of an object, including its class name.

5. **Methods**:
   - **`area`**: Placeholder method for calculating the area. It provides a default message indicating that the area calculation is not implemented in the base class.
   - **`info`**: Prints the `color` and `borderWidth` of the shape.
   - **`displayCount`**: Prints the total number of `Shape` objects created.

6. **String Representation (`__str__` method)**:
   - Provides a string representation of the `Shape` object, including its `color` and `borderWidth`.

### Usage:
- This `Shape` class can be used as a base class for other geometric shapes (e.g., `Circle`, `Rectangle`) that will inherit its attributes and methods.
- The `area` method can be overridden by subclasses to provide specific implementations for different shapes.
- The `__str__` method is useful for providing a readable string representation of the object.

This class provides a framework for defining shapes and can be extended by more specific shape classes.
