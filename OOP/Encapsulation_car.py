
# Example of Abstraction
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com

class Car:
 def __init__(self):
       self.__updateSoftware()
 def drive(self):
       print('driving')
 def __updateSoftware(self):
       print('updating software')
redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.
