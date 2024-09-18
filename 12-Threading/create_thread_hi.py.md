यहाँ थ्रेड्स से फंक्शन को एक्सीक्यूट करने का कोड उदाहरण है:

```python
# थ्रेड्स से फंक्शन को एक्सीक्यूट किया जा सकता है।
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import threading
from threading import *

def first_thread():
    print("Hello I am Ram")
    return

def second_thread():
    print("Hello I am Shyam")
    return

# थ्रेड फंक्शन जिसमें आर्ग्युमेंट्स होते हैं
def hello_thread(name):
    print("Hello", name)
    return

# Thread क्लास को इनहेरिट करके एक क्लास बनाएं
class Hi(Thread):
    def run(self):
        for i in range(5):
            print(i, "Hi")

# थ्रेड्स बनाएं
t1 = threading.Thread(target=first_thread)
t2 = threading.Thread(target=second_thread)
t3 = threading.Thread(target=hello_thread, args=('Ajay',))
t4 = threading.Thread(target=hello_thread, args=('Vijay',))
t5 = Hi()

# थ्रेड्स को स्टार्ट करें
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# स्क्रिप्ट के एक्सिट होने से पहले थ्रेड्स को पूरा होने के लिए जोड़े
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
```

### स्पष्टीकरण:
- **`import threading`**: `threading` मॉड्यूल को इम्पोर्ट करता है, जो थ्रेड्स बनाने और मैनेज करने के लिए सपोर्ट प्रदान करता है।
- **`def first_thread():`** और **`def second_thread():`**: वे फंक्शन हैं जो अलग-अलग थ्रेड्स में चलाए जाएंगे।
- **`def hello_thread(name):`**: एक फंक्शन जो एक आर्ग्युमेंट लेता है और एक संदेश प्रिंट करता है।
- **`class Hi(Thread):`**: `Thread` से इनहेरिट करके `Hi` नाम की एक क्लास बनाता है और `run` मेथड को ओवरराइड करता है।
- **`t1`, `t2`, `t3`, `t4`, `t5`**: `Thread` या `Hi` के इंस्टेंस हैं, जो विभिन्न टारगेट फंक्शंस या मेथड्स के साथ कॉन्फ़िगर किए गए हैं।
- **`t1.start()`, `t2.start()`, `t3.start()`, `t4.start()`, `t5.start()`**: थ्रेड्स को स्टार्ट करता है, जिससे उनके टारगेट फंक्शंस एक साथ चलने लगते हैं।
- **`t1.join()`, `t2.join()`, `t3.join()`, `t4.join()`, `t5.join()`**: सभी थ्रेड्स के पूरा होने का इंतजार करता है, ताकि स्क्रिप्ट समाप्त होने से पहले सभी आउटपुट प्रिंट हो जाएं।
