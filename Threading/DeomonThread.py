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
    time.sleep(0.2)
    print("How are you Ram?")

def second_thread():
    print("Hello Shyam")
    time.sleep(0.2)
    print("how are you Shyam?")    

t1 = threading.Thread(target=first_thread, daemon='true')
t2 = threading.Thread(target=second_thread) 

t1.start()
t2.start() 

