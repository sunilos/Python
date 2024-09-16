# Example of Exception Handling with Finally() Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

def hello():
    try:
        return 1
    finally:
        return 2
k = hello()
print(k)  #The finally block is executed even there is a return statement in the try block.
