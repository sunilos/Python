
```python
# शून्य से भाग देने की त्रुटि को संभालने का उदाहरण
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

try:  
    num1 = int(input("पहला नंबर दर्ज करें: "))  
    num2 = int(input("दूसरा नंबर दर्ज करें: "))  
    num3 = num1 / num2;  
    print("num1 / num2 = ", num3)  
except ZeroDivisionError:  
    print("शून्य से भाग नहीं दे सकते")  
else:  
    print("नमस्ते, मैं else ब्लॉक हूँ")
```

### व्याख्या:
- **`try` ब्लॉक**:
  - उपयोगकर्ता से दो नंबरों के लिए कहता है और उन्हें भाग देने की कोशिश करता है।
  - यदि दूसरा नंबर शून्य होता है, तो `ZeroDivisionError` उत्पन्न होता है।

- **`except ZeroDivisionError` ब्लॉक**:
  - `ZeroDivisionError` को पकड़ता है और एक त्रुटि संदेश प्रिंट करता है।

- **`else` ब्लॉक**:
  - यदि `try` ब्लॉक में कोई अपवाद उत्पन्न नहीं होता है, तो यह ब्लॉक कार्यान्वित होता है और एक संदेश प्रिंट करता है जो बताता है कि `else` ब्लॉक कार्यान्वित हुआ।

