यहाँ कोड है जो एक ऑब्जेक्ट को फ़ाइल में सीरियलाइज़ करने के लिए `pickle` लाइब्रेरी का उपयोग करता है:

```python
# एक ऑब्जेक्ट को फ़ाइल में सीरियलाइज़ करने का उदाहरण।
# पिकल लाइब्रेरी का उपयोग सीरियलाइजेशन और डेसीरियलाइजेशन के लिए किया जाता है

import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)

# Employee का एक उदाहरण बनाएं
e = Employee(1, 'Mayank', 1000, 'Indore')

# ऑब्जेक्ट को फ़ाइल में सीरियलाइज़ करें
with open('emp.dat', 'wb') as f:
    pickle.dump(e, f)
    print("Employee ऑब्जेक्ट का पिकलिंग पूरा हो गया")
```

### व्याख्या:
- **`import pickle`**: `pickle` लाइब्रेरी को इम्पोर्ट करता है, जो Python ऑब्जेक्ट्स को सीरियलाइज़ (पिकल) और डेसीरियलाइज़ (अनपिकल) करने के लिए उपयोग की जाती है।
- **`class Employee:`**: `Employee` क्लास को परिभाषित करता है जिसमें `__init__` मेथड से एट्रीब्यूट्स को इनिशियलाइज़ किया जाता है और `display` मेथड से कर्मचारी के विवरण को प्रिंट किया जाता है।
- **`e = Employee(1, 'Mayank', 1000, 'Indore')`**: `Employee` क्लास का एक उदाहरण बनाता है जिसमें निर्दिष्ट एट्रीब्यूट्स होते हैं।
- **`with open('emp.dat', 'wb') as f:`**: फ़ाइल `emp.dat` को राइट-बाइनरी मोड (`'wb'`) में खोलता है।
- **`pickle.dump(e, f)`**: `Employee` ऑब्जेक्ट `e` को सीरियलाइज़ करता है और इसे `emp.dat` फ़ाइल में लिखता है।
- **`print("Employee ऑब्जेक्ट का पिकलिंग पूरा हो गया")`**: सीरियलाइजेशन पूरा होने के बाद एक पुष्टि संदेश प्रिंट करता है।
