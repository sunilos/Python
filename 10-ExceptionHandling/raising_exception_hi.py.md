
```python
# एक साधारण अपवाद उठाने का उदाहरण
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

number = int(input("अपना नंबर दर्ज करें: "))
if number > 10:
    raise Exception('x 10 से अधिक नहीं होना चाहिए। नंबर का मान था: {}'.format(number))
```

### व्याख्या:
- **`number = int(input("अपना नंबर दर्ज करें: "))`**:
  - उपयोगकर्ता से एक नंबर दर्ज करने के लिए कहता है और इसे एक पूर्णांक में परिवर्तित करता है।

- **`if number > 10:`**:
  - यह जांचता है कि दर्ज किया गया नंबर 10 से अधिक है या नहीं।

- **`raise Exception(...)`**:
  - यदि शर्त सही है, तो एक `Exception` उठाता है और एक कस्टम त्रुटि संदेश प्रदान करता है।
  - संदेश में उस नंबर का मान शामिल होता है जिसने अपवाद को उत्पन्न किया।

