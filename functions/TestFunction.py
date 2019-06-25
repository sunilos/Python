# Example of Python Functions using def keyword
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Function definition
def sum( a,b ):
   "It sumd two numbers"
   print('a',a,'b',b)
   c = a + b
   return c;

print(sum(5,10))
print(sum(10,20))

#keyword argument 
d = sum(b=7,a=8)

#Pass by reference
def chageList( list ):
   list.append(6);
   print (list)
   return

list = [1,2,3,4,5]
print(list)
chageList(list)
print(list)

#Variable length 
def sumnum( a, *varg ):
   t = a
   for n in varg:
      t+=n
   return t;

total = sumnum(1,2,3,4,5)
print('Total', total)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(fname):
  print(fname + " Gupta")

my_function("John")
my_function("Amy")
my_function("Linus")


#passing a List as parameter

print("Ouput show passing value as a parameter : ")
def my_function(food):
 for x in food:
   print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return value as parameter

print("Ouput show Return value as Parameter are : ")
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
