# Example of  Abstract Method 
# This Example show that how one Method overrides another methods by same name
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

from abc import ABC,abstractmethod 
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
  

#run the program
tri_obj  = Triangle()
tri_obj.noofsides()

penta_obj  = Pentagon()
penta_obj.noofsides()
