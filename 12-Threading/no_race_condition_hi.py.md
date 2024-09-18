यहां एक अपडेटेड कोड उदाहरण है जो थ्रेड्स को `join` मेथड का उपयोग करके सिंक्रोनाइज करता है:

```python
# join मेथड का उपयोग करके सिंक्रोनाइज़्ड थ्रेड्स का उदाहरण
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
        self.lock = Lock()  # थ्रेड्स को सिंक्रोनाइज़ करने के लिए एक लॉक ऑब्जेक्ट बनाएं

    def get_balance(self):
        with self.lock:  # बैलेंस तक पहुँचने से पहले लॉक प्राप्त करें
            sleep(2)
            return self.balance

    def set_balance(self, amount):
        with self.lock:  # बैलेंस सेट करने से पहले लॉक प्राप्त करें
            sleep(2)
            self.balance = amount
  
    def deposit(self, amount):
        with self.lock:  # बैलेंस को संशोधित करने से पहले लॉक प्राप्त करें
            bal = self.get_balance()
            self.set_balance(bal + amount)

# Thread क्लास से इनहेरिट करके एक क्लास बनाएं
class Racing(Thread):
    def __init__(self, account, name):   # __init__ मेथड क्लास के कंस्ट्रक्टर का अनुकरण करता है
        super().__init__()
        self.account = account 
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
            print(self.name, self.account.get_balance())
        
def main_task():       
    acc = Account()        
    # थ्रेड इंस्टेंस बनाएं
    t1 = Racing(acc, "Ram")
    t2 = Racing(acc, "Shyam")

    # थ्रेड्स को शुरू करें
    t1.start()
    t2.start()

    # थ्रेड्स के पूरा होने का इंतजार करें
    t1.join()
    t2.join()

    print("Finish")

# मुख्य कार्य चलाएं
main_task()
```

### व्याख्या:
1. **लॉक ऑब्जेक्ट**: `Account` क्लास में एक `Lock` ऑब्जेक्ट बनाया गया है। इसका उपयोग साझा संसाधन (`balance`) तक पहुँच को सिंक्रोनाइज़ करने के लिए किया जाता है, ताकि रेस कंडीशन से बचा जा सके।
2. **कॉंटेक्स्ट मैनेजर (`with` स्टेटमेंट)**: `with self.lock` स्टेटमेंट का उपयोग बैलेंस एट्रिब्यूट तक पहुँचने या संशोधित करने से पहले लॉक प्राप्त करने के लिए किया जाता है। यह सुनिश्चित करता है कि एक समय में केवल एक ही थ्रेड महत्वपूर्ण भाग तक पहुँच सके।
3. **`join` मेथड**: `join` मेथड का उपयोग दोनों थ्रेड्स के पूरा होने का इंतजार करने के लिए किया जाता है, इसके बाद "Finish" प्रिंट किया जाता है। यह सुनिश्चित करता है कि मुख्य प्रोग्राम थ्रेड्स के काम खत्म होने से पहले समाप्त न हो।

यह कोड यह सुनिश्चित करता है कि `balance` एट्रिब्यूट थ्रेड-सुरक्षित तरीके से एक्सेस और संशोधित किया जाए, जिससे कई थ्रेड्स द्वारा एक साथ एक्सेस करने के कारण डेटा करप्शन की संभावनाएं कम हो जाती हैं।