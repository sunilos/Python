# Example of Creating Constructor  
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 
class Employee:  
    def __init__(self,name,id,email):   #the method __init__ simulates the constructor of the class. 
        self.id = id;  
        self.name = name;
        self.email = email;  
    def display (self):  
        print("ID: %d \nName: %s\nEmail : %s"%(self.id,self.name,self.email))  
emp1 = Employee("Ram",101, "a@gmail.com")  
emp2 = Employee("Shyam",102,"b@gmail.com")    
#accessing display() method to print employee 1 information     
emp1.display();    
#accessing display() method to print employee 2 information  
emp2.display();  