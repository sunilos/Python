# Example of simple Try Except with NameError
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

#The try block will generate a NameError, because Ram is not defined:
try:
    print(name)
except NameError:
  print("Variable name is not defined")
except:
  print("Something else went wrong")
