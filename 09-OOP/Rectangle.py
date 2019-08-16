from Shape import *
class Rectangle(Shape):

   def __init__(self, length, width , c='', b=0):
      self.length = length
      self.width = width
      super(Rectangle,self).__init__(c,b)
        
   def area(self):
      return self.length * self.length

   def __str__( self ):
      return "Rectangle: Length %d Width %d"  % (self.length,self.width) + " " + super(Rectangle,self).__str__()
