# Example of Creating Synchronise thread  using join method
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


from time import sleep
from threading import *

#Create a class by inheriting Thread class
class Hello(Thread):
   def run(self):
    for i in range(20):
        print(i, "Ram")
        
#Create a class by inheriting Thread class
class Hi(Thread):
  def run(self):
   for i in range(20):
         print(i, "Shyam")
        
#create thread instances 
t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")
