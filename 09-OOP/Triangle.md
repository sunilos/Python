Here is the code example for the `Triangle` class that inherits from the `Shape` class:

```python
from Shape import *

class Triangle(Shape):

    def __init__(self, base, height, c='', b=0):
        super().__init__(c, b)  # Initialize the base class
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return "Triangle: Base %d Height %d" % (self.base, self.height)
```

### Explanation:
- **`__init__` Method**:
  - Initializes the `Triangle` object with `base`, `height`, `color`, and `borderWidth`.
  - Calls the `__init__` method of the `Shape` class using `super()` to initialize `color` and `borderWidth`.

- **`area()` Method**:
  - Calculates and returns the area of the triangle using the formula \(\frac{1}{2} \times \text{base} \times \text{height}\).

- **`__str__()` Method**:
  - Provides a string representation of the `Triangle` object, including its `base` and `height`.

This code assumes that the `Shape` class is properly defined and available for import, as demonstrated in your previous examples.