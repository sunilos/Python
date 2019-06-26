# Example of Split String using split()
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import re 
string = "The rain in Spain" 

result1 = re.split("\s", string)
result2 = re.split("\s", string, 1)
print(result1)
print(result2)
