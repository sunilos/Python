# define child class
from Shape import *
class Circle(Shape):
   PI = 3.14

   def __init__(self, r, c='', b=0): #Constructer receiving two parameters 
      self.radius = r   #Instance variable
      self.color = c
      self.borderWidth = b
       
   def area(self):
      return self.radius * self.radius  * Circle.PI
