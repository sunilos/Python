# Example of Creating Multiple  Thread
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import threading

def first_thread():
    print("Hello Ram")
    return

def second_thread():
    print("Hello Shyam")    
    return


for i in range(20):
  thread_list1 = threading.Thread(target = first_thread)
  thread_list2 = threading.Thread(target = second_thread)

  thread_list1.start()
  thread_list2.start()