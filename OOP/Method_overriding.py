# Example of Method overriding
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#   
class Subject:  
    def calc(self):  
        print("Ram")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak(