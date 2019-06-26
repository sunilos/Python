# Example of Creating Thread in Group using join() mrthod
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
     # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 5)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Ram", 1)
thread2 = myThread(2, "Shyam", 2)

# Start new Threads
thread1.start()
thread2.start()
# Wait for all threads to complete
for t in threads:
    t.join()
#print("Exiting Main Thread")