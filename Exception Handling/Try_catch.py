# Example of simple Try Catch Exception
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 
# try:  
#    number   = int(input("Enter Number "))
#    number%2 == 0
#    print("Number is Even")
  
# except Exception:  
#     print("Number is Odd")  

try:
 
    number=int(input('Your Number '))
 
except:
 
    print ('Enter a Number.')
 
else:
 
    eve_or_odd = number%2 == 0
 
    if eve_or_odd:
 
        print('Number is Even .')
 
    else:
 
        print('Number is Odd')
