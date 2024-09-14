Here's the provided code with the example of the `Rectangle` class inheriting from the `Shape` class:

```python
from Shape import *

class Rectangle(Shape):

   def __init__(self, length, width , c='', b=0):
      self.length = length
      self.width = width
      super(Rectangle, self).__init__(c, b)
        
   def area(self):
      return self.length * self.width

   def __str__(self):
      return "Rectangle: Length %d Width %d" % (self.length, self.width) + " " + super(Rectangle, self).__str__()
```

### Explanation:

1. **Inheritance**:
   - **`Rectangle`** class inherits from **`Shape`** class, gaining its attributes and methods.

2. **Constructor (`__init__` method)**:
   - Initializes `length` and `width` as instance variables.
   - Calls the constructor of the parent `Shape` class using `super()`, passing `c` and `b` for `color` and `borderWidth`.

3. **Area Calculation**:
   - **`area`** method calculates the area of the rectangle using the formula: `length * width`.

4. **String Representation (`__str__` method)**:
   - **`__str__`** method provides a string representation of the `Rectangle` object.
   - It combines a description of the `Rectangle` with the description provided by the `Shape` class's `__str__` method using `super()`.

### Notes:
- **Constructor (`__init__`)**: Calls the `Shape` class's constructor to ensure the `Rectangle` object is properly initialized with `color` and `borderWidth`.
- **Area Calculation**: Corrected the formula to use `length * width` instead of `length * length`.
- **String Representation**: Combines the `Rectangle` description with the `Shape` class's description to provide a complete string representation.

This code assumes that the `Shape` class provides its own `__str__` method and relevant attributes. If `Shape` includes methods like `area` or `__str__`, these are overridden or extended by the `Rectangle` class.