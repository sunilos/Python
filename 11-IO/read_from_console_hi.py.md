यहाँ कोड है जो कंसोल से इनपुट पढ़ता है और उसे प्रिंट करता है:

```python
# कंसोल से इनपुट पढ़ने का उदाहरण
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# कंसोल से नाम पढ़ें
name = input("\nEnter your name: ")  # उपयोगकर्ता से उनका नाम दर्ज करने के लिए प्रेरित करता है
print("Your name is ", name)  # दर्ज किए गए नाम के साथ संदेश प्रिंट करता है
```

### व्याख्या:
- **`name = input("\nEnter your name: ")`**: `input` फ़ंक्शन प्रॉम्प्ट मैसेज दिखाता है और उपयोगकर्ता से कुछ टाइप करने की प्रतीक्षा करता है। दर्ज की गई वैल्यू को `name` वेरिएबल में स्टोर किया जाता है।
- **`print("Your name is ", name)`**: यह संदेश के साथ `name` की वैल्यू प्रिंट करता है जो उपयोगकर्ता ने दर्ज की है।

यह कोड उपयोगकर्ता से उनका नाम दर्ज करने के लिए कहेगा और फिर उसे कंसोल पर दिखाएगा।