यहाँ कोड के साथ टिप्पणियाँ और संक्षिप्त व्याख्या दी गई है:

```python
# def कीवर्ड का उपयोग करके पाइथन फंक्शन्स का उदाहरण
#
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @वेबसाइट www.SunilOs.com
#

# फंक्शन परिभाषा
def sum(a, b):
    """
    यह फंक्शन दो नंबरों का योग लौटाता है।
    """
    print('a:', a, 'b:', b)  # a और b के मान प्रिंट करें
    c = a + b                # योग की गणना करें
    return c                 # परिणाम लौटाएँ

# स्थानिक तर्कों के साथ sum फंक्शन को कॉल करना
print(sum(5, 10))  # आउटपुट: 15
print(sum(10, 20)) # आउटपुट: 30

# कीवर्ड तर्कों का उपयोग करके sum फंक्शन को कॉल करना
d = sum(b=7, a=8)  # आउटपुट: 15

# पास बाय रेफरेंस का उदाहरण
def changeList(lst):
    """
    यह फंक्शन सूची में एक मान जोड़ता है और सूची को प्रिंट करता है।
    """
    lst.append(6)    # सूची में 6 जोड़ें
    print(lst)       # संशोधित सूची प्रिंट करें
    return

# एक सूची परिभाषित करें और इसे changeList फंक्शन को पास करें
lst = [1, 2, 3, 4, 5]
print(lst)         # आउटपुट: [1, 2, 3, 4, 5]
changeList(lst)    # सूची को संशोधित करें
print(lst)         # आउटपुट: [1, 2, 3, 4, 5, 6]

# वेरिएबल लम्बाई के तर्कों के साथ फंक्शन
def sumnum(a, *varg):
    """
    यह फंक्शन एक नंबर और अतिरिक्त नंबरों की अनिश्चित संख्या का योग लौटाता है।
    """
    t = a
    for n in varg:
        t += n
    return t

# कई तर्कों के साथ sumnum फंक्शन को कॉल करना
total = sumnum(1, 2, 3, 4, 5)
print('Total:', total)  # आउटपुट: 15

# एकल पैरामीटर के साथ फंक्शन का उदाहरण
def my_function(x):
    return 5 * x

print(my_function(3))  # आउटपुट: 15
print(my_function(5))  # आउटपुट: 25
print(my_function(9))  # आउटपुट: 45

# एकल पैरामीटर और स्ट्रिंग जोड़ने के साथ फंक्शन का उदाहरण
def my_function(fname):
    print(fname + " Gupta")

my_function("John")   # आउटपुट: John Gupta
my_function("Amy")    # आउटपुट: Amy Gupta
my_function("Linus")  # आउटपुट: Linus Gupta

# एक सूची को पैरामीटर के रूप में पास करना
print("सूची को पैरामीटर के रूप में पास करने का आउटपुट:")
def my_function(food):
    for x in food:
        print(x)

fruits = ["Ram", "Shyam", "Jerry"]
my_function(fruits)

# फंक्शन से मान लौटाना
print("फंक्शन से लौटाए गए मान का आउटपुट:")
def my_function(x):
    return 5 * x

print(my_function(3))  # आउटपुट: 15
print(my_function(5))  # आउटपुट: 25
print(my_function(9))  # आउटपुट: 45
```

### व्याख्या:

1. **फंक्शन परिभाषा**:
   - `def sum(a, b)`: एक फंक्शन परिभाषित करता है जो दो पैरामीटर `a` और `b` को लेता है, उनका योग करता है और परिणाम लौटाता है।
   - `def changeList(lst)`: एक फंक्शन परिभाषित करता है जो सूची को एक मान जोड़कर संशोधित करता है और उसे प्रिंट करता है।
   - `def sumnum(a, *varg)`: एक फंक्शन परिभाषित करता है जो एक निश्चित पैरामीटर `a` और कई अतिरिक्त पैरामीटर को लेता है, उनका योग करता है और लौटाता है।

2. **फंक्शन्स को कॉल करना**:
   - `sum(5, 10)`: `sum` फंक्शन को स्थानिक तर्क `5` और `10` के साथ कॉल करता है।
   - `sum(b=7, a=8)`: `sum` फंक्शन को कीवर्ड तर्कों के साथ कॉल करता है, जिससे यह दिखाता है कि तर्कों का क्रम नाम द्वारा निर्दिष्ट किया जा सकता है।
   - `changeList(lst)`: एक सूची को फंक्शन में पास करना और उसे संशोधित करना दिखाता है।
   - `sumnum(1, 2, 3, 4, 5)`: कई तर्कों के साथ `sumnum` फंक्शन को कॉल करता है।

3. **वेरिएबल लम्बाई के तर्क**:
   - `sumnum` फंक्शन `*varg` का उपयोग करके किसी भी संख्या में अतिरिक्त तर्क लेता है।

4. **स्ट्रिंग जोड़ना और सूची पास करना**:
   - `my_function(fname)` और `my_function(food)` विभिन्न तरीकों से स्ट्रिंग्स और सूचियों को संभालने के उदाहरण दिखाते हैं।

5. **रिटर्न वैल्यूज़**:
   - `my_function(x)` यह दिखाता है कि फंक्शन से मान कैसे लौटाए जाते हैं और उन्हें आगे की गणनाओं में कैसे उपयोग किया जा सकता है।

यह कोड पाइथन में विभिन्न फंक्शन अवधारणाओं को कवर करता है, जैसे स्थानिक और कीवर्ड तर्क, पास बाय रेफरेंस, वेरिएबल लम्बाई के तर्क, और रिटर्न वैल्यूज़।