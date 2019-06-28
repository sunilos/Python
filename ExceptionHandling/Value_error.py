# Example of Try Exception with ValueError
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  
import sys

print("Lets fix the previous code with exception handling")

try:
    number = int(input("Enter the  number "))

except ValueError:
    print("Enter Numbers Only")
    sys.exit()

print("You entered number ", number)