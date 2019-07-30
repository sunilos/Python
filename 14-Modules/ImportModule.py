# Example of Creating  Modules 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

from Calculations import summation    
#it will import only the summation() from calculation.py  
a = int(input("Enter the first number "))  
b = int(input("Enter the second number "))  
print("Sum = ",summation(a,b)) #we do not need to specify the module name while accessing summation()  