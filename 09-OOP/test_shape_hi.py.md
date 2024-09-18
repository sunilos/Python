यहाँ दिए गए कोड और उसकी व्याख्या का सरल हिंदी अनुवाद है:

```python
# क्लास का उदाहरण

# Shape क्लास को टेस्ट करें
from Shape import *
from Circle import *
from Triangle import *
from Rectangle import *

def testShape():
    'Shape क्लास को टेस्ट करें'
    # Shape क्लास के ऑब्जेक्ट बनाएं 
    s1 = Shape("Red", 5)
    s2 = Shape("Blue", 10)

    print('ऑब्जेक्ट S1')
    c = s1.color
    print('Color एट्रिब्यूट: ', c)
    s1.info()
    print('एरिया', s1.area())
    print('ID', id(s1))  # मेमोरी में ऑब्जेक्ट का रेफरेंस दिखाता है

    print("--------------------")
    print('ऑब्जेक्ट S2')
    s2.info()
    print('एरिया', s2.area())
    print('ID', id(s2))  # मेमोरी में ऑब्जेक्ट का रेफरेंस दिखाता है

    print("--------------------")    
    print('कुल Shapes ', s2.count)
    print('कुल Shapes ', Shape.count)

    # ऑब्जेक्ट्स को डिलीट कर दें
    del s1
    del s2

def displayShapeMetadata():
    print("--------------------")
    print("Shape मेटाडेटा")
    print("Shape.__doc__:", Shape.__doc__)
    print("Shape.__name__:", Shape.__name__)
    print("Shape.__module__:", Shape.__module__)
    print("Shape.__bases__:", Shape.__bases__)
    print("Shape.__dict__:", Shape.__dict__)

def testCircle():
    c1 = Circle(2, 'Red', 5)
    c2 = Circle(3, 'Blue')
    c3 = Circle(4)

    print("ऑब्जेक्ट C1")
    print('Color', c1.color)
    print('Border Width', c1.borderWidth)
    print("सर्कल का एरिया है ", c1.area())
    print(c1.__dict__)

    print("C1:", c1)
    print("C2:", c2)
    print("C3:", c3)
    print("Shape की संख्या ", Shape.count)    

def testTriangle():
    t1 = Triangle(10, 5)

    print("ऑब्जेक्ट T1")
    print("त्रिभुज का एरिया है ", t1.area())
    print(t1)
    print(t1.__dict__)

def testRectangle():
    r1 = Rectangle(5, 10, 'Red', 6)

    print("ऑब्जेक्ट R1")
    print("आयत का एरिया है ", r1.area())
    print(r1)
    print(r1.__dict__)

# क्लास को टेस्ट करने के लिए फंक्शन कॉल्स अन-कमेंट करें
# testShape()
displayShapeMetadata()
# testCircle()
# testTriangle()
# testRectangle()
```

### व्याख्या:

- **`testShape()`**: 
  - यह `Shape` क्लास के ऑब्जेक्ट्स बनाता है, उनके एट्रिब्यूट्स दिखाता है, और उनका एरिया प्रिंट करता है।
  - इसमें क्लास एट्रिब्यूट्स और ऑब्जेक्ट्स का मेटाडेटा एक्सेस और डिस्प्ले करने का तरीका बताया गया है।

- **`displayShapeMetadata()`**: 
  - यह `Shape` क्लास का मेटाडेटा दिखाता है, जिसमें उसकी डॉक्यूमेंटेशन, नाम, मॉड्यूल, बेस क्लासेस, और एट्रिब्यूट्स की डिक्शनरी शामिल हैं।

- **`testCircle()`**: 
  - यह `Circle` क्लास के ऑब्जेक्ट्स बनाता है और उनके एट्रिब्यूट्स और एरिया दिखाता है।
  - इसमें `__str__` और `__dict__` का उपयोग कर ऑब्जेक्ट का स्ट्रिंग रिप्रेजेंटेशन और एट्रिब्यूट्स की डिक्शनरी प्राप्त करने का तरीका बताया गया है।

- **`testTriangle()`**: 
  - यह `Triangle` क्लास का एक ऑब्जेक्ट बनाता है और उसका एरिया और एट्रिब्यूट्स दिखाता है।

- **`testRectangle()`**: 
  - यह `Rectangle` क्लास का एक ऑब्जेक्ट बनाता है और उसका एरिया और एट्रिब्यूट्स प्रिंट करता है।

### नोट:
- जिन क्लासेस को टेस्ट करना है, उनके फंक्शन कॉल्स (`testShape()`, `testCircle()`, `testTriangle()`, `testRectangle()`) को अन-कमेंट करें और कोड चलाएं।
