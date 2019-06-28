# Example of   Abstract Method 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 
from abc import ABC, abstractmethod
class Polygon(ABC):
   def noofsides(self):
        pass
class Triangle(Polygon):
 # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
  
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
  
class Hexagon(Polygon):
   # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):  
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

tri_obj  = Triangle()
tri_obj.noofsides()
qua_obj = Quadrilateral()
qua_obj.noofsides()
penta_obj  = Pentagon()
penta_obj.noofsides()
hexa_obj  = Hexagon()
penta_obj.noofsides()
