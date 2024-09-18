यहाँ Python में एक मॉड्यूल बनाने और उसका उपयोग करने का उदाहरण है:

```python
# मॉड्यूल बनाने का उदाहरण
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com 
#

# Calculations मॉड्यूल से summation फ़ंक्शन को आयात करना
from Calculations import summation    

# यह 'calculation.py' नामक फ़ाइल से केवल summation() फ़ंक्शन को आयात करता है, जो 'Calculations' मॉड्यूल में है

# उपयोगकर्ता से दो इनपुट नंबर लेना
a = int(input("पहला नंबर दर्ज करें "))  # इनपुट स्ट्रिंग को एक पूर्णांक में परिवर्तित करता है
b = int(input("दूसरा नंबर दर्ज करें "))  # इनपुट स्ट्रिंग को एक पूर्णांक में परिवर्तित करता है

# summation() फ़ंक्शन को कॉल करना और परिणाम को प्रिंट करना
print("योग = ", summation(a, b))  
# यहाँ, हम सीधे summation() फ़ंक्शन को कॉल करते हैं बिना मॉड्यूल नाम का उल्लेख किए (जैसे, Calculations.summation())
```

### व्याख्या:

1. **मॉड्यूल बनाना और उपयोग करना**:
   - यह उदाहरण दिखाता है कि Python में मॉड्यूल कैसे बनाया और उपयोग किया जाता है।
   - Python में एक मॉड्यूल एक फ़ाइल होती है जिसमें फ़ंक्शंस, क्लासेस, या वेरिएबल्स होते हैं जिन्हें विभिन्न प्रोग्रामों में आयात करके पुनः उपयोग किया जा सकता है।

2. **आयात स्टेटमेंट**:
   - `from Calculations import summation`: यह लाइन `Calculations` मॉड्यूल से `summation()` फ़ंक्शन को आयात करती है (यह फ़ाइल `calculation.py` नाम की होती है)।
   - केवल विशिष्ट फ़ंक्शन को आयात करके, आप अपने कोड में सीधे `summation()` का उपयोग कर सकते हैं बिना मॉड्यूल नाम के उपसर्ग के (जैसे, `Calculations.summation()`).

3. **उपयोगकर्ता से इनपुट**:
   - `input()` उपयोगकर्ता से एक नंबर दर्ज करने के लिए कहता है। `int()` फ़ंक्शन का उपयोग इनपुट स्ट्रिंग को पूर्णांक में बदलने के लिए किया जाता है ताकि गणितीय संचालन किए जा सकें।

4. **फ़ंक्शन कॉल करना**:
   - उपयोगकर्ता से `a` और `b` इनपुट लेने के बाद, `summation(a, b)` फ़ंक्शन को कॉल करके दो नंबरों को जोड़ा जाता है।
   - परिणाम को `print()` के माध्यम से `योग = परिणाम` के स्वरूप में प्रिंट किया जाता है।

### मान्यताएँ:
- `Calculations` मॉड्यूल (जिसे `calculation.py` फ़ाइल कहा जाता है) में एक `summation()` फ़ंक्शन होता है जो दो नंबरों को जोड़ता है।
- संरचना इस प्रकार होगी:
   ```
   Calculations/
       └── calculation.py
   ```

### उपयोग का उदाहरण:

यदि आप इस प्रोग्राम को चलाते हैं और नंबर 5 और 10 इनपुट करते हैं:
```bash
पहला नंबर दर्ज करें 5
दूसरा नंबर दर्ज करें 10
योग = 15
```