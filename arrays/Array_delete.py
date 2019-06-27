# Example of Array List to delete Existing Element
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

from array import *
array_list = array('i', [10,20,30,40,50])
array_list.remove(30)
for x in array_list:
 print(x)