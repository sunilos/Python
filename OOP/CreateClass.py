# Example of Creating class 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 
class Employee:  
    id = 10;  
    name = "Ram"  
    def display (self):  
        print("ID:%d\nName:%s"%(self.id,self.name))  

emp = Employee()
emp.display()