यहाँ `Triangle` क्लास का उदाहरण है, जो `Shape` क्लास से इनहेरिट करता है:

```python
from Shape import *

class Triangle(Shape):

    def __init__(self, base, height, c='', b=0):
        super().__init__(c, b)  # बेस क्लास को इनिशियलाइज़ करें
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return "Triangle: Base %d Height %d" % (self.base, self.height)
```

### व्याख्या:
- **`__init__` मेथड**:
  - यह मेथड `Triangle` ऑब्जेक्ट को इनिशियलाइज़ करता है, जिसमें `base`, `height`, `color`, और `borderWidth` होते हैं।
  - `super()` का उपयोग करके, यह `Shape` क्लास के `__init__` मेथड को कॉल करता है ताकि `color` और `borderWidth` इनिशियलाइज़ हो सके।

- **`area()` मेथड**:
  - यह मेथड त्रिभुज का क्षेत्रफल \(\frac{1}{2} \times \text{base} \times \text{height}\) के फार्मूले से गणना करता है और वापस करता है।

- **`__str__()` मेथड**:
  - यह मेथड `Triangle` ऑब्जेक्ट का स्ट्रिंग रिप्रेजेंटेशन प्रदान करता है, जिसमें उसकी `base` और `height` शामिल हैं।

यह कोड मानता है कि `Shape` क्लास पहले से सही ढंग से परिभाषित और इंपोर्ट के लिए उपलब्ध है, जैसा कि आपके पिछले उदाहरणों में दिखाया गया है।
