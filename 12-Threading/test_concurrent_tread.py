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

def my_thread(name):
  for i in range(500):
    print( i, 'Hello ', name)  
      
t1 = threading.Thread(target = my_thread, args=("Ram",))
t2 = threading.Thread(target =  my_thread, args=("Shyam",))
t1.start()
t2.start()
