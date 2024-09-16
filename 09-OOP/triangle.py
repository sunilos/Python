from Shape import *
class Triangle(Shape):

   def __init__(self, base, height , c='', b=0): 
      self.base = base
      self.height = height
      self.color = c
      self.borderWidth = b
        
   def area(self):
      return (self.base * self.height) /2 

   def __str__( self ):
      return "Triangle: Base %d Hieght %d"  % (self.base,self.height) 
