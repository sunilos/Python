# Example of Array to Insert Element using Index Array
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Aray Insertion

from array import *
array_list = array('i', [10,20,30,40,50])
array_list.insert(1,60)
for x in array_list:
 print(x)