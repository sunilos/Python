# Example of Thread
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import _thread

# Define a function for the thread
def info(threadName):
        for i in range (1,100) :
                print ( i, threadName )
                #time.sleep(2)

                
def testThrad():
        try:
           _thread.start_new_thread( info, ("Thread-1",))
           _thread.start_new_thread( info, ("Thread-2",))

        except:
           print ("Error: unable to start thread")

testThrad()
