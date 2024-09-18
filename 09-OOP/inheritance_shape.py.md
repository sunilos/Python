
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
    count = 0  # Class variable to keep track of the number of Shape instances

    def __init__(self, c, b):
        """
        Constructor to initialize the Shape object with color and border width.
        """
        self.color = c  # Instance variable for color
        self.borderWidth = b  # Instance variable for border width
        Shape.count += 1  # Increment class variable count

    def __del__(self):
        """
        Destructor to print a message when an object is destroyed.
        """
        className = self.__class__.__name__
        print("Destroying", className)

    def area(self):
        """
        Method to calculate the area of the shape. This is a placeholder method to be overridden by subclasses.
        """
        print("I don't know how to calculate area")
        return -1

    def info(self):
        """
        Method to print the color and border width of the shape.
        """
        print("Color:", self.color)
        print("Border Width:", self.borderWidth)

    def displayCount(self):
        """
        Method to print the total number of Shape instances.
        """
        print("Total Shape", Shape.count)

    def __str__(self):
        """
        Method to return a string representation of the shape.
        """
        return "Shape: Color %s Border Width %i" % (self.color, self.borderWidth)


# Define child class Circle that inherits from Shape
class Circle(Shape):
    PI = 3.14  # Class variable for the value of PI

    def __init__(self, r, c='', b=0):
        """
        Constructor to initialize the Circle object with radius, color, and border width.
        """
        self.radius = r  # Instance variable for radius
        self.color = c
        self.borderWidth = b

    def area(self):
        """
        Method to calculate the area of the circle.
        """
        return self.radius * self.radius * Circle.PI

    def __str__(self):
        """
        Method to return a string representation of the circle.
        """
        return "Circle: Radius %d" % self.radius


# Define child class Triangle that inherits from Shape
class Triangle(Shape):

    def __init__(self, base, height, c='', b=0):
        """
        Constructor to initialize the Triangle object with base, height, color, and border width.
        """
        self.base = base  # Instance variable for base
        self.height = height  # Instance variable for height
        self.color = c
        self.borderWidth = b

    def area(self):
        """
        Method to calculate the area of the triangle.
        """
        return (self.base * self.height) / 2

    def __str__(self):
        """
        Method to return a string representation of the triangle.
        """
        return "Triangle: Base %d Height %d" % (self.base, self.height)


# Define child class Rectangle that inherits from Shape
class Rectangle(Shape):

    def __init__(self, length, width, c='', b=0):
        """
        Constructor to initialize the Rectangle object with length, width, color, and border width.
        """
        self.length = length  # Instance variable for length
        self.width = width  # Instance variable for width
        super(Rectangle, self).__init__(c, b)  # Call the constructor of the parent class Shape

    def area(self):
        """
        Method to calculate the area of the rectangle.
        """
        return self.length * self.width

    def __str__(self):
        """
        Method to return a string representation of the rectangle.
        """
        return "Rectangle: Length %d Width %d" % (self.length, self.width) + " " + super(Rectangle, self).__str__()
```

### Explanation:

1. **Base Class (`Shape`)**:
   - `Shape` is the base class with attributes for color and border width.
   - It has a class variable `count` to keep track of the number of instances created.
   - `__init__` initializes the instance and increments the `count`.
   - `__del__` is a destructor that prints a message when an object is destroyed.
   - `area` is a placeholder method to be overridden by subclasses.
   - `info` prints the color and border width.
   - `displayCount` prints the total number of Shape instances.
   - `__str__` returns a string representation of the Shape object.

2. **Child Classes**:
   - **`Circle`**:
     - Inherits from `Shape`.
     - Adds a `radius` attribute and calculates the area using `PI`.
     - Overrides `__str__` to include radius information.
   
   - **`Triangle`**:
     - Inherits from `Shape`.
     - Adds `base` and `height` attributes and calculates the area.
     - Overrides `__str__` to include base and height information.
   
   - **`Rectangle`**:
     - Inherits from `Shape`.
     - Adds `length` and `width` attributes and calculates the area.
     - Uses `super()` to call the parent class's constructor and includes `color` and `borderWidth` in its string representation.

### Inheritance:
- The `Circle`, `Triangle`, and `Rectangle` classes inherit from the `Shape` class, demonstrating how derived classes can extend and customize the behavior of a base class.
