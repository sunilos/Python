# Deamon Thread are supporting threads.  It can be created using  daemon='true' attribute.
# Garbage collector is the best example of deamon thread.
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import threading
import time

def first_thread():
    print("Hello Ram")
    for i in range(20):
     time.sleep(100)
     print("How are you Ram?")

def second_thread():
    print("Hello Shyam")
    for i in range(20):
     time.sleep(2)
     print("how are you Shyam?")    

t1 = threading.Thread(target=first_thread, daemon='true')
t2 = threading.Thread(target=second_thread) 

t1.start()
time.sleep(2)
t2.start() 

