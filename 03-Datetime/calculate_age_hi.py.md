

```python
from datetime import date  # 'datetime' लाइब्रेरी से 'date' मॉड्यूल को आयात करना

# जन्मतिथि के आधार पर उम्र की गणना करने के लिए फ़ंक्शन
def calculateAge(birthDate): 
    today = date.today()  # आज की तारीख प्राप्त करना
    # उम्र की गणना: वर्तमान वर्ष से जन्म वर्ष घटाना
    # यदि जन्म महीने और दिन इस साल अब तक नहीं आए हैं तो गणना को समायोजित करना
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age  # गणना की गई उम्र लौटाना

# जन्म वर्ष, महीना, और दिन के लिए उपयोगकर्ता से इनपुट लेना
year = int(input("Enter your Birth Year = "))  # जन्म वर्ष इनपुट लेना
month = int(input("Enter your Birth Month = "))  # जन्म महीना इनपुट लेना
day = int(input("Enter your Birth Day = "))  # जन्म दिन इनपुट लेना

# 'calculateAge' फ़ंक्शन को कॉल करके उम्र की गणना करना
age = calculateAge(date(year, month, day))

# उम्र को वर्षों में प्रिंट करना
print(age, "years")  # आउटपुट: उपयोगकर्ता की उम्र वर्षों में
```

### स्पष्टीकरण:

1. **मॉड्यूल आयात करना**:
   - Python की `datetime` लाइब्रेरी से `date` मॉड्यूल को आयात किया जाता है ताकि तारीखों के साथ काम किया जा सके।

2. **फ़ंक्शन परिभाषा**:
   - `calculateAge(birthDate)`: यह फ़ंक्शन उपयोगकर्ता की उम्र की गणना करता है वर्तमान तारीख (`today`) और दी गई जन्मतिथि (`birthDate`) की तुलना करके।
   - `((today.month, today.day) < (birthDate.month, birthDate.day))` यह चेक करता है कि उपयोगकर्ता का जन्मदिन इस साल अब तक आया है या नहीं; अगर नहीं, तो गणना की गई उम्र में एक वर्ष घटा देता है।

3. **उपयोगकर्ता इनपुट**:
   - प्रोग्राम उपयोगकर्ता से जन्म वर्ष, महीना, और दिन के लिए इनपुट लेता है और उन्हें पूर्णांक में परिवर्तित करता है।

4. **उम्र की गणना**:
   - `calculateAge()` फ़ंक्शन को जन्मतिथि के साथ कॉल किया जाता है, और परिणाम को `age` वेरिएबल में संग्रहित किया जाता है।

5. **आउटपुट**:
   - प्रोग्राम गणना की गई उम्र को "years" के साथ प्रिंट करता है। उदाहरण के लिए, अगर उपयोगकर्ता की उम्र 25 वर्ष है, तो आउटपुट होगा `25 years`।
