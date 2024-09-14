Here's the code with added comments and a brief explanation:

```python
# Example of Creating Constructor  
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

class Employee:
    def __init__(self, name, id, email):
        """
        Constructor for the Employee class.
        
        Parameters:
        name (str): Name of the employee.
        id (int): ID of the employee.
        email (str): Email of the employee.
        """
        self.id = id          # Instance variable for employee ID
        self.name = name      # Instance variable for employee name
        self.email = email    # Instance variable for employee email

    def display(self):
        """
        Display the details of the employee.
        """
        print("ID: %d \nName: %s\nEmail: %s" % (self.id, self.name, self.email))

# Creating instances of the Employee class
emp1 = Employee("Ram", 101, "a@gmail.com")
emp2 = Employee("Shyam", 102, "b@gmail.com")

# Accessing display() method to print employee 1 information     
emp1.display()

# Accessing display() method to print employee 2 information  
emp2.display()
```

### Explanation:

1. **Class Definition**:
   - `class Employee:`: Defines a class named `Employee`.

2. **Constructor**:
   - `def __init__(self, name, id, email)`: The constructor method `__init__` is called when an instance of the class is created. It initializes the instance variables with the values provided.
   - `self.id = id`: Sets the instance variable `id` to the value provided.
   - `self.name = name`: Sets the instance variable `name` to the value provided.
   - `self.email = email`: Sets the instance variable `email` to the value provided.

3. **Method**:
   - `def display(self)`: Defines a method to display the employee details.
   - `print("ID: %d \nName: %s\nEmail: %s" % (self.id, self.name, self.email))`: Prints the employee details in a formatted string.

4. **Creating Instances**:
   - `emp1 = Employee("Ram", 101, "a@gmail.com")`: Creates an instance of `Employee` with the name "Ram", ID 101, and email "a@gmail.com".
   - `emp2 = Employee("Shyam", 102, "b@gmail.com")`: Creates another instance of `Employee` with the name "Shyam", ID 102, and email "b@gmail.com".

5. **Accessing Methods**:
   - `emp1.display()`: Calls the `display` method on the `emp1` instance to print its details.
   - `emp2.display()`: Calls the `display` method on the `emp2` instance to print its details.

This example demonstrates how to define and use a constructor in a class to initialize instance variables and how to define and use methods to interact with these variables.