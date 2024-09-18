Here's the code with added comments and a brief explanation:

```python
# Define child class
from Shape import *  # Importing the Shape class from the Shape module

class Circle(Shape):
    PI = 3.14  # Class-level constant for the value of PI

    def __init__(self, r, c='', b=0):
        """
        Constructor for the Circle class.
        
        Parameters:
        r (float): Radius of the circle.
        c (str): Color of the circle (default is an empty string).
        b (int): Border width of the circle (default is 0).
        """
        self.radius = r          # Instance variable to store the radius
        self.color = c           # Instance variable to store the color
        self.borderWidth = b     # Instance variable to store the border width

    def area(self):
        """
        Calculate and return the area of the circle.
        
        Returns:
        float: Area of the circle.
        """
        return self.radius * self.radius * Circle.PI  # Using the formula for the area of a circle
```

### Explanation:

1. **Class Definition**:
   - `from Shape import *`: Imports the `Shape` class from the `Shape` module. This assumes that there is a `Shape` class defined in a separate file named `Shape.py`.

2. **Circle Class**:
   - `class Circle(Shape)`: Defines a `Circle` class that inherits from the `Shape` class. This means `Circle` will have all the attributes and methods of `Shape`, unless they are overridden.

3. **Class-level Constant**:
   - `PI = 3.14`: Defines a constant `PI` for use in the area calculation. This value is associated with the class rather than instances.

4. **Constructor**:
   - `def __init__(self, r, c='', b=0)`: The constructor method initializes the `Circle` object with a radius (`r`), color (`c`), and border width (`b`). It sets instance variables for these attributes.
   - `self.radius = r`: Sets the instance variable `radius` to the value provided.
   - `self.color = c`: Sets the instance variable `color` to the value provided.
   - `self.borderWidth = b`: Sets the instance variable `borderWidth` to the value provided.

5. **Method**:
   - `def area(self)`: Defines a method to calculate the area of the circle.
   - `return self.radius * self.radius * Circle.PI`: Calculates the area using the formula \( \text{Area} = \pi \times r^2 \) and returns it.

This class demonstrates how to use inheritance and encapsulation in Python to extend functionality from a base class (`Shape`) and add specific features to a derived class (`Circle`).
