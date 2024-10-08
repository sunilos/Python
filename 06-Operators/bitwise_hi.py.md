
```python
# बिटवाइज़ ऑपरेटर का उदाहरण
# 
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @वेबसाइट www.SunilOs.com
#

# वेरिएबल्स को प्रारंभ करें
a = 60            # 60 बाइनरी में: 0011 1100
b = 13            # 13 बाइनरी में: 0000 1101
c = 0

# बिटवाइज़ AND
c = a & b         # 60 & 13 = 12 (बाइनरी में: 0000 1100)
print("Line 1 - c का मान है", c)  # आउटपुट 12 होगा

# बिटवाइज़ OR
c = a | b         # 60 | 13 = 61 (बाइनरी में: 0011 1101)
print("Line 2 - c का मान है", c)  # आउटपुट 61 होगा

# बिटवाइज़ XOR
c = a ^ b         # 60 ^ 13 = 49 (बाइनरी में: 0011 0001)
print("Line 3 - c का मान है", c)  # आउटपुट 49 होगा

# बिटवाइज़ NOT
c = ~a            # ~60 = -61 (बाइनरी में: 1100 0011, बिटवाइज़ NOT बिट्स को इनवर्ट करता है)
print("Line 4 - c का मान है", c)  # आउटपुट -61 होगा

# बिटवाइज़ लेफ्ट शिफ्ट
c = a << 2        # 60 << 2 = 240 (बाइनरी में: 1111 0000, बिट्स को 2 स्थानों पर बाईं ओर शिफ्ट करता है)
print("Line 5 - c का मान है", c)  # आउटपुट 240 होगा

# बिटवाइज़ राइट शिफ्ट
c = a >> 2        # 60 >> 2 = 15 (बाइनरी में: 0000 1111, बिट्स को 2 स्थानों पर दाईं ओर शिफ्ट करता है)
print("Line 6 - c का मान है", c)  # आउटपुट 15 होगा
```

### व्याख्या:

1. **प्रारंभिककरण**:
   - `a = 60` (बाइनरी में: `0011 1100`)
   - `b = 13` (बाइनरी में: `0000 1101`)

2. **बिटवाइज़ AND (`&`)**:
   - `a & b` का परिणाम `12` है (बाइनरी में: `0000 1100`), जहां बिट्स केवल तब `1` होते हैं जब दोनों ऑपरेण्ड में `1` होते हैं।

3. **बिटवाइज़ OR (`|`)**:
   - `a | b` का परिणाम `61` है (बाइनरी में: `0011 1101`), जहां बिट्स `1` होते हैं अगर वे किसी भी ऑपरेण्ड में `1` होते हैं।

4. **बिटवाइज़ XOR (`^`)**:
   - `a ^ b` का परिणाम `49` है (बाइनरी में: `0011 0001`), जहां बिट्स `1` होते हैं अगर ऑपरेण्ड अलग होते हैं।

5. **बिटवाइज़ NOT (`~`)**:
   - `~a` का परिणाम `-61` है (बाइनरी में: `1100 0011`). बिटवाइज़ NOT सभी बिट्स को इनवर्ट करता है।

6. **बिटवाइज़ लेफ्ट शिफ्ट (`<<`)**:
   - `a << 2` बिट्स को बाईं ओर 2 स्थानों पर शिफ्ट करता है, परिणाम `240` है (बाइनरी में: `1111 0000`).

7. **बिटवाइज़ राइट शिफ्ट (`>>`)**:
   - `a >> 2` बिट्स को दाईं ओर 2 स्थानों पर शिफ्ट करता है, परिणाम `15` है (बाइनरी में: `0000 1111`).

