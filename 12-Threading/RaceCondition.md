Here's the updated code with the corrected use of thread synchronization and the proper application of `Lock` for thread safety:

```python
# Example of Creating Synchronized Threads using the join method
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

from time import sleep
from threading import *
import threading

class Account:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Create a lock object for synchronizing threads

    def get_balance(self):
        with self.lock:  # Acquire the lock before accessing the balance
            sleep(2)
            return self.balance

    def set_balance(self, amount):
        with self.lock:  # Acquire the lock before setting the balance
            sleep(2)
            self.balance = amount
  
    def deposit(self, amount):
        with self.lock:  # Acquire the lock before modifying the balance
            bal = self.get_balance()
            self.set_balance(bal + amount)

# Create a class by inheriting Thread class
class Racing(Thread):
    def __init__(self, account, name):
        super().__init__()
        self.account = account 
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
            print(self.name, self.account.get_balance())
        
def main_task():       
    acc = Account()        
    # Create thread instances 
    t1 = Racing(acc, "Ram")
    t2 = Racing(acc, "Shyam")

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    print("Finish")

# Run main task
main_task()
```

### Key Points:
1. **Lock Object**: A `Lock` object is created in the `Account` class to ensure that only one thread can execute critical sections of code (like modifying the `balance`) at a time.

2. **Context Manager (`with` statement)**: Using the `with self.lock` statement ensures that the lock is acquired before accessing or modifying the `balance` and is automatically released after the block of code is executed.

3. **`join` Method**: The `join` method is used to wait for the completion of both threads before printing "Finish". This ensures the main thread does not exit before the worker threads have finished their tasks.

This setup ensures that the `balance` attribute is updated safely and correctly even when multiple threads are working simultaneously.