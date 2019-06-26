# Example of Multi Threading
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import threading

def first_thread():
    print("Hello I am thread")
    return
threads = []
for i in range(20):
    thread_list = threading.Thread(target = first_thread)
    threads.append(thread_list)
    thread_list.start()

