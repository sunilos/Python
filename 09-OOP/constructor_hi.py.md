
```python
# कंस्ट्रक्टर बनाने का उदाहरण  
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

class Employee:
    def __init__(self, name, id, email):
        """
        Employee क्लास का कंस्ट्रक्टर।
        
        पैरामीटर्स:
        name (str): कर्मचारी का नाम।
        id (int): कर्मचारी का ID।
        email (str): कर्मचारी का ईमेल।
        """
        self.id = id          # कर्मचारी ID के लिए इंस्टेंस वेरिएबल
        self.name = name      # कर्मचारी नाम के लिए इंस्टेंस वेरिएबल
        self.email = email    # कर्मचारी ईमेल के लिए इंस्टेंस वेरिएबल

    def display(self):
        """
        कर्मचारी के विवरण को प्रदर्शित करें।
        """
        print("ID: %d \nName: %s\nEmail: %s" % (self.id, self.name, self.email))

# Employee क्लास के इंस्टेंस बनाना
emp1 = Employee("Ram", 101, "a@gmail.com")
emp2 = Employee("Shyam", 102, "b@gmail.com")

# display() मेथड का उपयोग करके कर्मचारी 1 की जानकारी प्रिंट करें     
emp1.display()

# display() मेथड का उपयोग करके कर्मचारी 2 की जानकारी प्रिंट करें  
emp2.display()
```

### व्याख्या:

1. **क्लास परिभाषा**:
   - `class Employee:`: एक `Employee` नाम की क्लास को परिभाषित करता है।

2. **कंस्ट्रक्टर**:
   - `def __init__(self, name, id, email)`: कंस्ट्रक्टर मेथड `__init__` को तब कॉल किया जाता है जब क्लास का एक इंस्टेंस बनाया जाता है। यह इंस्टेंस वेरिएबल्स को प्रदान किए गए मानों से इनिशियलाइज करता है।
   - `self.id = id`: `id` इंस्टेंस वेरिएबल को प्रदान किए गए मान पर सेट करता है।
   - `self.name = name`: `name` इंस्टेंस वेरिएबल को प्रदान किए गए मान पर सेट करता है।
   - `self.email = email`: `email` इंस्टेंस वेरिएबल को प्रदान किए गए मान पर सेट करता है।

3. **मेथड**:
   - `def display(self)`: एक मेथड को परिभाषित करता है जो कर्मचारी के विवरण को प्रदर्शित करता है।
   - `print("ID: %d \nName: %s\nEmail: %s" % (self.id, self.name, self.email))`: एक फॉर्मेटेड स्ट्रिंग में कर्मचारी के विवरण को प्रिंट करता है।

4. **इंस्टेंस बनाना**:
   - `emp1 = Employee("Ram", 101, "a@gmail.com")`: "Ram", ID 101, और ईमेल "a@gmail.com" के साथ `Employee` का एक इंस्टेंस बनाता है।
   - `emp2 = Employee("Shyam", 102, "b@gmail.com")`: "Shyam", ID 102, और ईमेल "b@gmail.com" के साथ एक और `Employee` का इंस्टेंस बनाता है।

5. **मेथड्स का उपयोग**:
   - `emp1.display()`: `emp1` इंस्टेंस पर `display` मेथड को कॉल करता है ताकि इसके विवरण को प्रिंट किया जा सके।
   - `emp2.display()`: `emp2` इंस्टेंस पर `display` मेथड को कॉल करता है ताकि इसके विवरण को प्रिंट किया जा सके।

