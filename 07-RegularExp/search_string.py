# Example to search string using search()
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#search matching string
import re

string = "The rain in Spain"
result = re.search('the', string)

if result:
   print("String Found ")
else:
   print("Not found")  
