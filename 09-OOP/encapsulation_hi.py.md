
```python
# कैप्सूलन बनाने का उदाहरण
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

class Person:
    def __init__(self):
        """
        Person ऑब्जेक्ट को इनिशियलाइज़ करने के लिए कन्स्ट्रक्टर।
        """
        # इंस्टेंस वेरिएबल
        self.name = "No name"

    def display(self, name):
        """
        प्रदान किए गए नाम के साथ एक ग्रीटिंग प्रदर्शित करने की विधि।
        """
        print("Hello", name)

# Person क्लास का एक इंस्टेंस बनाना
obj = Person()

# विभिन्न नामों के साथ display मेथड को कॉल करें
obj.display("Ram")   # आउटपुट: Hello Ram
obj.display("Shyam") # आउटपुट: Hello Shyam
```

### व्याख्या:

1. **क्लास परिभाषा**:
   - `class Person:`: एक `Person` नाम की क्लास को परिभाषित करता है।

2. **कन्स्ट्रक्टर (`__init__` मेथड)**:
   - `def __init__(self):`: कन्स्ट्रक्टर मेथड को परिभाषित करता है जो `Person` क्लास का एक नया इंस्टेंस इनिशियलाइज़ करता है।
   - `self.name = "No name"`: इंस्टेंस वेरिएबल `name` को डिफॉल्ट वैल्यू `"No name"` से इनिशियलाइज़ करता है। यह कैप्सूलन का एक साधारण उदाहरण है, क्योंकि `name` अट्रिब्यूट क्लास के अंदर है और इसे मेथड्स के माध्यम से सेट या मॉडिफाई किया जा सकता है।

3. **विधि**:
   - `def display(self, name):`: एक `display` मेथड को परिभाषित करता है जो एक अतिरिक्त पैरामीटर `name` लेता है और एक ग्रीटिंग संदेश प्रिंट करता है।
   - `print("Hello", name)`: प्रदान किए गए `name` के साथ ग्रीटिंग संदेश प्रिंट करता है।

4. **इंस्टेंस बनाना**:
   - `obj = Person()`: `Person` क्लास का एक इंस्टेंस बनाता है। `name` अट्रिब्यूट को `"No name"` से इनिशियलाइज़ किया जाता है।

5. **मेथड को कॉल करना**:
   - `obj.display("Ram")`: `display` मेथड को `"Ram"` तर्क के साथ कॉल करता है, जो `Hello Ram` प्रिंट करता है।
   - `obj.display("Shyam")`: `display` मेथड को `"Shyam"` तर्क के साथ कॉल करता है, जो `Hello Shyam` प्रिंट करता है।

