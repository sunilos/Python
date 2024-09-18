यहां कोड के साथ टिप्पणियाँ और एक संक्षिप्त व्याख्या दी गई है:

```python
# sub() का उपयोग करके मेल को अपने स्ट्रिंग के टेक्स्ट से बदलने का उदाहरण
#
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @वेबसाइट www.SunilOs.com
#

import re  # रेगुलर एक्सप्रेशंस मॉड्यूल को आयात करें

# एक स्ट्रिंग परिभाषित करें जिसे बदलना है
string = "The rain in Spain"

# सभी व्हाइटस्पेस कैरेक्टर्स (\s) को एक कॉमा और स्पेस से बदलें
result = re.sub("\s", " ,", string)

# बदली हुई स्ट्रिंग को प्रिंट करें
print(result)
```

### व्याख्या:

1. **`re` मॉड्यूल आयात करें**:
   - `import re`: `re` मॉड्यूल को आयात करता है, जो पायथन में रेगुलर एक्सप्रेशंस के साथ काम करने के लिए उपयोगी है।

2. **स्ट्रिंग परिभाषित करें**:
   - `string = "The rain in Spain"`: यह वह स्ट्रिंग है जिसमें बदलाव किए जाएंगे।

3. **मेल को बदलें**:
   - `result = re.sub("\s", " ,", string)`: `re.sub()` फ़ंक्शन का उपयोग पैटर्न `"\s"` (जो किसी भी व्हाइटस्पेस कैरेक्टर को मैच करता है) को `" ,"` से बदलने के लिए किया जाता है। `\s` पैटर्न में स्पेस, टैब और न्यूलाइन शामिल होते हैं।

4. **परिणाम प्रिंट करें**:
   - `print(result)`: यह बदली हुई स्ट्रिंग को प्रिंट करता है, जहां प्रत्येक व्हाइटस्पेस कैरेक्टर को एक कॉमा और स्पेस से बदल दिया गया है।

दिए गए स्ट्रिंग `"The rain in Spain"` के लिए, आउटपुट होगा:
```
The, rain, in, Spain
```

`re.sub()` फ़ंक्शन का उपयोग विशिष्ट पैटर्न से मेल खाने वाले सबस्ट्रिंग को नए सबस्ट्रिंग से बदलने के लिए किया जाता है।