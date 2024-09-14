Here's the code snippet for running multiple threads concurrently, with a function that prints messages from different threads:

```python
# Example of running multiple threads concurrently.  
# When you run this program, you will observe that 
# sometimes it will print "Ram" and sometimes it will print "Shyam"
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import threading

def my_thread(name):
    for i in range(500):
        print(i, 'Hello', name)  
      
# Create two threads
t1 = threading.Thread(target=my_thread, args=("Ram",))
t2 = threading.Thread(target=my_thread, args=("Shyam",))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
```

### Key Points:
- **Thread Creation**: Two threads are created, each running the `my_thread` function with different arguments ("Ram" and "Shyam").
- **Concurrency**: The `start()` method initiates the threads, which run concurrently. This means both threads will execute their tasks simultaneously.
- **Joining Threads**: The `join()` method ensures that the main thread waits for both threads to complete before exiting. This is useful for synchronization when you need to make sure that all threads have finished their work.

The output might interleave the prints from both threads, demonstrating concurrent execution.