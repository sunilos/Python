
```python
# Example of Class 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Test Shape class
from Shape import *
from Circle import *
from Triangle import *
from Rectangle import *

def testShape():
    'Test Shape class'
    # Create instances of Shape 
    s1 = Shape("Red", 5)
    s2 = Shape("Blue", 10)

    print('Object S1')
    c = s1.color
    print('Color attribute: ', c)
    s1.info()
    print('Area', s1.area())
    print('ID', id(s1))  # Display memory reference 

    print("--------------------")
    print('Object S2')
    s2.info()
    print('Area', s2.area())
    print('ID', id(s2))  # Display memory reference

    print("--------------------")    
    print('Total Shapes ', s2.count)
    print('Total Shapes ', Shape.count)

    # Garbage collect objects
    del s1
    del s2

def displayShapeMetadata():
    print("--------------------")
    print("Shape Metadata")
    print("Shape.__doc__:", Shape.__doc__)
    print("Shape.__name__:", Shape.__name__)
    print("Shape.__module__:", Shape.__module__)
    print("Shape.__bases__:", Shape.__bases__)
    print("Shape.__dict__:", Shape.__dict__)

def testCircle():
    c1 = Circle(2, 'Red', 5)
    c2 = Circle(3, 'Blue')
    c3 = Circle(4)

    print("Object C1")
    print('Color', c1.color)
    print('Border Width', c1.borderWidth)
    print("Area of Circle is ", c1.area())
    print(c1.__dict__)

    print("C1:", c1)
    print("C2:", c2)
    print("C3:", c3)
    print("Shape count ", Shape.count)    

def testTriangle():
    t1 = Triangle(10, 5)

    print("Object T1")
    print("Area of Triangle is ", t1.area())
    print(t1)
    print(t1.__dict__)

def testRectangle():
    r1 = Rectangle(5, 10, 'Red', 6)

    print("Object R1")
    print("Area of Rectangle is ", r1.area())
    print(r1)
    print(r1.__dict__)

# Uncomment the function calls to test the classes
# testShape()
displayShapeMetadata()
# testCircle()
# testTriangle()
# testRectangle()
```

### Explanation:

- **`testShape()`**: 
  - Creates instances of the `Shape` class, displays their attributes, and prints their area.
  - Demonstrates how to access and display class attributes and instance metadata.

- **`displayShapeMetadata()`**: 
  - Displays metadata about the `Shape` class, including its documentation, name, module, base classes, and dictionary of attributes.

- **`testCircle()`**: 
  - Creates instances of the `Circle` class and prints their attributes and area.
  - Shows how to use `__str__` and `__dict__` to get a string representation and dictionary of the instance's attributes.

- **`testTriangle()`**: 
  - Creates an instance of the `Triangle` class and displays its area and attributes.

- **`testRectangle()`**: 
  - Creates an instance of the `Rectangle` class and prints its area and attributes.

