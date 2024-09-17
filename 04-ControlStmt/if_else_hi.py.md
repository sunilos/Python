"यहाँ कोड में टिप्पणियाँ और संक्षिप्त विवरण जोड़ा गया है:

```python
# If-else नियंत्रण बयान का उदाहरण
#
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @Url www.SunilOs.com
#

# एक वस्तु की कीमत को स्टोर करने के लिए वेरिएबल
price = 99  # मान लीजिए कि एक वस्तु (इस मामले में, पिज्जा) की कीमत 99 है

# If-else नियंत्रण संरचना यह जांचने के लिए कि क्या कीमत 100 से कम है
if price < 100:
    # यह ब्लॉक तब चलेगा जब शर्त सही होगी (कीमत 100 से कम है)
    print("I can not buy Pizza")  # संदेश जो दिखाता है कि पिज्जा नहीं खरीदा जा सकता
    print("Feeling bad :(")  # एक उदास भावना
else:
    # यह ब्लॉक तब चलेगा जब शर्त गलत होगी (कीमत 100 या उससे अधिक है)
    print("I can buy Pizza")  # संदेश जो दिखाता है कि पिज्जा खरीदा जा सकता है
    print("Yu Yum :)")  # एक खुश भावना
```

### स्पष्टीकरण:

1. **वेरिएबल की प्रारंभिककरण**:
   - `price = 99`: एक वस्तु (पिज्जा) की कीमत `price` वेरिएबल में स्टोर की गई है।

2. **If-Else स्टेटमेंट**:
   - **शर्त**: `if` शर्त जांचती है कि क्या `price` 100 से कम है (`if price < 100:`)।
   - यदि शर्त सही है (यानी, कीमत 100 से कम है), तो `if` ब्लॉक का कोड चलेगा:
     - "I can not buy Pizza" और "Feeling bad :(" प्रिंट किया जाएगा जिससे निराशा व्यक्त होती है।
   - यदि शर्त गलत है (यानी, कीमत 100 या उससे अधिक है), तो `else` ब्लॉक का कोड चलेगा:
     - "I can buy Pizza" और "Yu Yum :)" प्रिंट किया जाएगा जिससे खुशी व्यक्त होती है।

3. **आउटपुट**:
   - चूंकि `price = 99` (जो कि 100 से कम है), प्रोग्राम `if` ब्लॉक को चलाएगा और प्रिंट करेगा:
     ```
     I can not buy Pizza
     Feeling bad :(
     ```

यह साधारण प्रोग्राम दिखाता है कि कैसे कंट्रोल फ्लो (if-else) निर्णय लेते हैं, एक शर्त के आधार पर।"