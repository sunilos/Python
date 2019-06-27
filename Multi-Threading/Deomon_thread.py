# Example of Deamon Thread
#
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

thread1 = threading.Thread(target=first_thread,daemon='true')
thread2 = threading.Thread(target=second_thread) 

thread1.start()
thread2.start() 

thread1.join()
thread2.join()