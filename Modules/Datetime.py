
# Example of Date Time
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com


import datetime

x = datetime.datetime.now()
print(x)


x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
x = datetime.datetime(2020, 5, 17)
print(x)
