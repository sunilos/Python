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


#The strftime() Method
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

