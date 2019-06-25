# Example of Date Time 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#
import datetime
#Import the datetime module and display the current date:

x = datetime.datetime.now()
print(x)

#Return the year and name of weekday:
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#To create a date, we can use the datetime() class (constructor) of the datetime module.
x = datetime.datetime(2020, 5, 17)
print(x)

#The strftime() Method
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

