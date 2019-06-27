# Example of Multiple Inheritance
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  
class addition:  
    def sum(self,a,b):  
        return a+b;  
class multiplication:  
    def multiply(self,a,b):  
        return a*b;  
class derived(addition,multiplication):   #derived class inherits both addition and mu,tiplacation base class
    def Divide(self,a,b):  
        return a/b;  

derived_obj = derived()  
print(derived_obj.sum(10,20))  
print(derived_obj.multiply(10,20))  
print(derived_obj.Divide(10,20))

d = {1:'Ram', 2:'Shyam', 3:'Balram', 4:'Raju'};   
print("1st name is "+d[1]);  
print("2nd name is "+ d[4]);  
print (d);  
print (d.keys());  
print (d.values()); 
