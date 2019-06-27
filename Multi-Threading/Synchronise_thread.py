# Example of Creating Thread in Group
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


from time import sleep
from threading import *

class Hello(Thread):
   def run(self):
    for i in range(20):
        print("Ram")
        

class Hi(Thread):
  def run(self):
   for i in range(20):
         print("Shyam")
        

thread1 = Hello()
thread2 = Hi()

thread1.start()
sleep(0.2)
thread2.start()

thread1.join()
thread2.join()
print("Bye")
