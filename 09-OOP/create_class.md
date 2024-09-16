Here's the code with added comments and a brief explanation:

```python
# Example of Creating class 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

class Employee:
    id = 10        # Class variable for employee ID
    name = "Ram"   # Class variable for employee name

    def display(self):
        """
        Display the details of the employee.
        """
        print("ID: %d\nName: %s" % (self.id, self.name))

# Create an instance of the Employee class
emp = Employee()

# Call the display() method to print employee details
emp.display()
```

### Explanation:

1. **Class Definition**:
   - `class Employee:`: Defines a class named `Employee`.

2. **Class Variables**:
   - `id = 10`: A class variable `id` is set with the value `10`. This is shared by all instances of the class.
   - `name = "Ram"`: A class variable `name` is set with the value `"Ram"`. This is also shared by all instances of the class.

3. **Method**:
   - `def display(self)`: Defines a method to display the employee details.
   - `print("ID: %d\nName: %s" % (self.id, self.name))`: Prints the employee ID and name. `self.id` and `self.name` refer to the class variables `id` and `name`, respectively.

4. **Creating an Instance**:
   - `emp = Employee()`: Creates an instance of the `Employee` class. The class variables `id` and `name` are available to this instance.

5. **Accessing Method**:
   - `emp.display()`: Calls the `display` method on the `emp` instance, which prints the employee details.

This example demonstrates how to create a class with class variables and methods, and how to access these variables and methods through an instance of the class. Note that `self` in the `display` method refers to the instance itself, allowing access to the class variables.
