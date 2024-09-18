
```python
# बिल्ट-इन फंक्शंस का उदाहरण

class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

# Student क्लास का एक ऑब्जेक्ट बनाते हैं  
s = Student("John", 101, 22)  

# ऑब्जेक्ट s के name एट्रिब्यूट को प्रिंट करता है  
print(getattr(s, 'name'))  # आउटपुट: John  

# age एट्रिब्यूट का मान 23 पर सेट करता है  
setattr(s, "age", 23)  

# age का संशोधित मान प्रिंट करता है  
print(getattr(s, 'age'))  # आउटपुट: 23  

# True प्रिंट करता है अगर ऑब्जेक्ट में id नाम का एट्रिब्यूट है  
print(hasattr(s, 'id'))  # आउटपुट: True  

# age एट्रिब्यूट को डिलीट कर देता है  
delattr(s, 'age')  

# यह एरर देगा क्योंकि age एट्रिब्यूट डिलीट कर दिया गया है  
print(s.age)  # AttributeError: 'Student' ऑब्जेक्ट में 'age' एट्रिब्यूट नहीं है
```

### व्याख्या:

1. **`getattr(object, name)`**:
   - यह फंक्शन `object` से `name` नाम के एट्रिब्यूट का मान प्राप्त करता है।
   - अगर एट्रिब्यूट मौजूद होता है, तो यह उसका मान लौटाता है; अगर नहीं होता, तो `AttributeError` उठाता है।

2. **`setattr(object, name, value)`**:
   - यह फंक्शन `object` के `name` एट्रिब्यूट का मान `value` पर सेट करता है।
   - अगर एट्रिब्यूट मौजूद नहीं होता, तो यह नया एट्रिब्यूट बना देता है।

3. **`hasattr(object, name)`**:
   - यह जांचता है कि क्या `object` में `name` नाम का एट्रिब्यूट है।
   - अगर एट्रिब्यूट मौजूद होता है, तो `True` लौटाता है, अन्यथा `False`।

4. **`delattr(object, name)`**:
   - यह `object` से `name` नाम के एट्रिब्यूट को हटा देता है।
   - अगर एट्रिब्यूट मौजूद नहीं होता, तो यह `AttributeError` उठाता है।

