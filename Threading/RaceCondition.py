# Example of Multi-Threads with  Race Condition using acquire() and release()  Method
# In this Example you will see first it will Hello Ram and Hello Shyam 
# Then You see it will print How are you Ram and Shyam concurrently
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#
 
import threading 
import time
  
def first_thread(name):
    
    lock = threading.Lock()
    print("Hello " , name)
   
    for i in range(30):
      lock.acquire()
      time.sleep(2)
      print("How are you " , name)
     
      lock.release()
  
def second_thread():
    
        t1 = threading.Thread(target=first_thread,args=["Ram"])
        t2 = threading.Thread(target=first_thread,args=["Shyam"])

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        
second_thread()

