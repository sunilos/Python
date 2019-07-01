# Example of running mutiple threads concurrently.  
# When you will run this program you will observe that 
# sometimes it will print Ram and sometimes it will print Shyam 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import threading
import time
def my_thread(name):
  for i in range(20):
    print('Hello ', name)  
      
t1 = threading.Thread(target = my_thread, args=("Ram",))
t2 = threading.Thread(target =  my_thread, args=("Shyam",))
t1.start()
time.sleep(2)
t2.start()

t1.join()
t2.join()
