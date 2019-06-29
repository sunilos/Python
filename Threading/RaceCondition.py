# Example of Creating Synchronise thread  
# In this Program you will see first time it print Ram and Shyam 
# And then  after it will print Ram and Shyam  continously and at last it print Bye by main thread
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import threading
import time
 
class MyThread(threading.Thread):
    def __init__(self,threadId, name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    

    def run(self):
       print("Hello  " + self.name) 
       #Get Lock to synchronise Thread
       threadLock.acquire()
       get(self.name,self.counter,3)
        #Free The Lock to release Next Thread
       threadLock.release()


def get(threadName,delay,counter):
    while counter:
     time.sleep(delay)
     print(threadName)
     counter -= 1
threadLock = threading.Lock()
threads = []

t1 =  MyThread(1,"Ram",1)
t2 = MyThread(2,"Shyam",2)

t1.start()
t2.start()
t1.join()
t2.join()
print("Bye")