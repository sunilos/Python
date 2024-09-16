Here's the code with added comments and a brief explanation:

```python
# Example of Abstract Method 
# This example shows how one method can override another method with the same name
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

from abc import ABC, abstractmethod

# Abstract class definition
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        """
        Abstract method that should be overridden in derived classes.
        """
        pass

# Derived class that implements the abstract method
class Triangle(Polygon):
    def noofsides(self):
        """
        Override the abstract method to provide specific implementation.
        """
        print("I have 3 sides")

# Another derived class that implements the abstract method
class Pentagon(Polygon):
    def noofsides(self):
        """
        Override the abstract method to provide specific implementation.
        """
        print("I have 5 sides")

# Run the program
tri_obj = Triangle()
tri_obj.noofsides()  # Output: I have 3 sides

penta_obj = Pentagon()
penta_obj.noofsides()  # Output: I have 5 sides
```

### Explanation:

1. **Abstract Base Class (ABC)**:
   - `from abc import ABC, abstractmethod`: Imports the necessary components for defining abstract classes.
   - `class Polygon(ABC)`: Defines an abstract base class named `Polygon` that inherits from `ABC` (Abstract Base Class).
   - `@abstractmethod`: A decorator that marks the method `noofsides` as abstract, meaning it must be implemented by any subclass of `Polygon`.

2. **Derived Classes**:
   - `class Triangle(Polygon)`: Defines a subclass of `Polygon` that overrides the `noofsides` method to print a specific message.
   - `class Pentagon(Polygon)`: Another subclass of `Polygon` that provides its own implementation of the `noofsides` method.

3. **Method Overriding**:
   - Both `Triangle` and `Pentagon` classes provide their own implementation of the `noofsides` method, which was declared abstract in the `Polygon` class.

4. **Running the Program**:
   - `tri_obj = Triangle()`: Creates an instance of the `Triangle` class and calls the overridden `noofsides` method.
   - `penta_obj = Pentagon()`: Creates an instance of the `Pentagon` class and calls the overridden `noofsides` method.

This code demonstrates the concept of abstract methods in Python, where an abstract base class defines a method that must be implemented by its subclasses, and how different subclasses can provide their own specific implementations of that method.
