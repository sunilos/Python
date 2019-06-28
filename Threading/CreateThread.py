# A function can be executed from inside a thread.
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import threading

def first_thread():
    print("Hello I am Ram")
    return

def second_thread():
    print("Hello I am Shyam")
    return

#Thread function with arguments
def hello_thread(name):
    print("Hello", name)
    return

#Create a thread 
t1 = threading.Thread(target = first_thread)
t2 = threading.Thread(target = second_thread)
t3 = threading.Thread(target = hello_thread, args=('Ajay',))
t4 = threading.Thread(target = hello_thread, args=('Vijay',))

#Start a thread 
t1.start()
t2.start()
t3.start()
t4.start()
