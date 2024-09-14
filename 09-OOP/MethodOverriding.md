Here's the provided code with explanations for method overriding:

```python
# Example of Method Overriding
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#   

class Animal:
    def sound(self):
        """
        Method to represent the sound an animal makes.
        This is the base class method.
        """
        print('Animal makes sound.')

class Dog(Animal):
    def sound(self):
        """
        Method to represent the sound a dog makes.
        This method overrides the sound method in the Animal class.
        """
        print('Dog barks.')

# Create an instance of the Dog class
d = Dog()
# Call the overridden method
d.sound()
```

### Explanation:

1. **Base Class (`Animal`)**:
   - `Animal` is the base class with a method `sound` that prints "Animal makes sound."

2. **Derived Class (`Dog`)**:
   - `Dog` inherits from `Animal`.
   - It overrides the `sound` method to print "Dog barks" instead of the message from the base class.

3. **Method Overriding**:
   - In `Dog`, the `sound` method overrides the `sound` method from the `Animal` class.
   - When `d.sound()` is called, the `sound` method of the `Dog` class is executed, demonstrating method overriding.

### Key Points:
- **Method Overriding**: Allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
- **Polymorphism**: Method overriding is a way to achieve polymorphism in object-oriented programming, where a subclass can have a different behavior for a method than its superclass.