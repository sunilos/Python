# Example of Creating Thread
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

for i in range(20):
    thread_list = threading.Thread(target = first_thread)
    thread_list.start()

