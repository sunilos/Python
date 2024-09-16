Here's the code example demonstrating the use of built-in functions with class attributes:

```python
# Example of Built-in Functions 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

# Creates an object of the class Student  
s = Student("John", 101, 22)  

# Prints the attribute name of the object s  
print(getattr(s, 'name'))  # Output: John  

# Resets the value of attribute age to 23  
setattr(s, "age", 23)  

# Prints the modified value of age  
print(getattr(s, 'age'))  # Output: 23  

# Prints True if the student contains the attribute with name id  
print(hasattr(s, 'id'))  # Output: True  

# Deletes the attribute age  
delattr(s, 'age')  

# This will give an error since the attribute age has been deleted  
print(s.age)  # Raises AttributeError: 'Student' object has no attribute 'age'
```

### Explanation:

1. **`getattr(object, name)`**:
   - Retrieves the value of the attribute named `name` from the object `object`.
   - If the attribute exists, it returns its value; otherwise, it raises an `AttributeError`.

2. **`setattr(object, name, value)`**:
   - Sets the value of the attribute named `name` on the object `object` to the specified `value`.
   - If the attribute does not exist, it will be created.

3. **`hasattr(object, name)`**:
   - Checks if the object `object` has an attribute named `name`.
   - Returns `True` if the attribute exists, otherwise `False`.

4. **`delattr(object, name)`**:
   - Deletes the attribute named `name` from the object `object`.
   - If the attribute does not exist, it raises an `AttributeError`.

### Usage:
- These built-in functions are useful for dynamically interacting with an object's attributes, especially when dealing with objects where attribute names may not be known until runtime.
