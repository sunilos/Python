Here's the updated code for synchronizing threads using the `join` method:

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

class Account:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()  # Create a lock object for synchronizing threads

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
    def __init__(self, account, name):   # The method __init__ simulates the constructor of the class. 
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

### Explanation:
1. **Lock Object**: A `Lock` object is created in the `Account` class. This is used to synchronize access to the shared resource (`balance`) to prevent race conditions.
2. **Context Manager (`with` statement)**: The `with self.lock` statement is used to acquire the lock before accessing or modifying the `balance` attribute. This ensures that only one thread can access the critical section at a time.
3. **`join` Method**: The `join` method is used to wait for both threads to complete before printing "Finish". This ensures that the main program does not exit before the threads have finished their work.

This code ensures that the `balance` attribute is accessed and modified in a thread-safe manner, avoiding potential data corruption due to simultaneous access by multiple threads.
