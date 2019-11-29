# Example of Date Time 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#
import datetime
#Import the datetime module and display the current date:

# get current datetime 
x = datetime.datetime.now()
print(x)

#Get year and name of weekday:
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


# Get object of given date 
x = datetime.datetime(2018, 6, 1)

# format date using strftime() method. Get name of month
print(x.strftime("%B"))

