# Example of Built-in class attributes
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  
class Student:  
    'Hello'
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
s = Student("John",101,22)  
print(Student.__doc__)   #This gives us the class documentation if documentation is present. None otherwise.
print(Student.__name__) #it will print class name
print(s.__dict__)  #This is a dictionary holding the class namespace. 
print(s.__module__)  #it will print class module