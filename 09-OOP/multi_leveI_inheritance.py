# Example of  Multilevel Inheritance 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Define a class as 'student'
class Student:
    # Method
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

# Define a class as 'test' and inherit base class 'student'
class Test(Student):
    # Method
    def getMarks(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))

# Define a class as 'marks' and inherit derived class 'test'
class Marks(Test):
    # Method
    def display(self):
        print("\n\nName: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Study in: ",self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)


m1 = Marks()
# Call base class method 'getStudent()'
m1.getStudent()
# Call first derived class method 'getMarks()'
m1.getMarks()
# Call second derived class method 'display()'
m1.display()
