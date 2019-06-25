# Example of Exception Handling 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Python program to handle simple runtime error
a = [1, 2, 3]
try:
  print("Second element = %d" %(a[1]))

  # Throws error since there are only 3 elements in array
  print("Fourth element = %d" %(a[3]))

except IndexError:
  print("An error occurred")

#Program to handle multiple errors with one except statement
print("Program to handle multiple errors with one except statement : ")
def AbyB(a , b):
  try:
    c = ((a+b) / (a-b))
  except ZeroDivisionError:
    print("a/b result in 0")
  else:
    print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Raising Exception

# Program to depict Raising Exception

try:
  raise NameError("Hi there") # Raise Error
except NameError:
  print("An exception")
  raise # To determine whether the exception was raised or not