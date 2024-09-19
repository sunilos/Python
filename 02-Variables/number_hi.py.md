

```python
# संख्याओं के प्रकार जानने का उदाहरण
#
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @Url www.SunilOs.com
#

# एक पूर्णांक मान के साथ वेरिएबल बनाना
a = 10  # 'a' को 10 का पूर्णांक मान दिया जा रहा है
print("The type of variable having value", a, "is", type(a))  # आउटपुट: The type of variable having value 10 is <class 'int'>

# एक फ्लोट मान के साथ वेरिएबल बनाना
b = 10.2345  # 'b' को 10.2345 का फ्लोट मान दिया जा रहा है
print("The type of variable having value", b, "is", type(b))  # आउटपुट: The type of variable having value 10.2345 is <class 'float'>

# एक जटिल (complex) मान के साथ वेरिएबल बनाना
c = 100 + 3j  # 'c' को 100 + 3j का जटिल मान दिया जा रहा है
print("The type of variable having value", c, "is", type(c))  # आउटपुट: The type of variable having value (100+3j) is <class 'complex'>
```

### स्पष्टीकरण:

1. **पूर्णांक प्रकार**:
   - वेरिएबल `a` को 10 का पूर्णांक मान दिया गया है। `type(a)` फ़ंक्शन `a` के प्रकार की जाँच करता है, जो `<class 'int'>` होता है।

2. **फ्लोट प्रकार**:
   - वेरिएबल `b` को 10.2345 का फ्लोट मान दिया गया है। `type(b)` फ़ंक्शन `b` के प्रकार की जाँच करता है, जो `<class 'float'>` होता है।

3. **जटिल प्रकार**:
   - वेरिएबल `c` को 100 + 3j का जटिल मान (जहाँ `j` काल्पनिक इकाई को दर्शाता है) दिया गया है। `type(c)` फ़ंक्शन `c` के प्रकार की जाँच करता है, जो `<class 'complex'>` होता है।

4. **आउटपुट**:
   - `print()` स्टेटमेंट्स प्रत्येक वेरिएबल का मान और उसके प्रकार (`int`, `float`, `complex`) दिखाते हैं।
