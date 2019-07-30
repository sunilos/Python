# Example of Try Exception with ValueError  
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

while True:  
    try:
        x = int(input("Please enter a number: "))
        print("%s squared is %s" % (x, x**5))
    except ValueError:
        print("Please enter a only Number!")