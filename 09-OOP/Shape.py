
# Example of Inhetitance 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

class Shape:
   'Shape expert class contains shape related attributes and methods'
   count = 0 #Class variable

   #Define constructor using __init__ method
   def __init__(self, c, b): #Constructer receiving two parameters 
      self.color = c   #Instance variable
      self.borderWidth = b #Instance variable
      Shape.count += 1 #Increase count

   #Define destructor using __del__ method
   def __del__(self):
      className = self.__class__.__name__
      print ("Destroying ", className )

   #Calculate area of Shape
   def area(self):   
     print ("I dont know how to calculate area")
     return -1

   #Print info of Shape
   def info(self):   
     print ("Color: %s" % self.color)
     print ("Border Width: %s" % self.borderWidth)

   #Define a method 
   def displayCount(self):
     print ("Total Shape %d", Shape.count)

   def __str__( self ):
     return "Circle: Color %s Border Width %i"  % (self.color,self.borderWidth) 
     
