# Example of Array List to delete Existing Element
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Array Deletion
from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
 print(x)