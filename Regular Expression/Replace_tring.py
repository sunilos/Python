# Example of sub() replaces the matches with text of your string
#

# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import re 
string = "The rain in Spain"
result = re.sub("\s", " ,", string)
print(result)
