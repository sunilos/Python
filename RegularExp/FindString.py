# Example to find string using findall() 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import re

string = "The rain in Spain"
result = re.findall("ai", string) 
print(result)
if (result):
 print("YES! We have a match!")
else:
 print("No match")