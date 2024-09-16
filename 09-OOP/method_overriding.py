# Example of Method overriding
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#   

class Animal:
   def sound(self):
      print('Animal makes sound.')
 
class Dog(Animal):
   def sound(self):
      print('Dog barks.')
 
d = Dog()
d.sound()
