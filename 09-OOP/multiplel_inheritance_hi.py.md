यहाँ दिए गए कोड और उसकी व्याख्या का सरल हिंदी अनुवाद है:

```python
# Multiple Inheritance का उदाहरण

class Addition:
    def sum(self, a, b):
        """
        दो संख्याओं का योग लौटाने का तरीका।
        """
        return a + b

class Multiplication:
    def multiply(self, a, b):
        """
        दो संख्याओं का गुणनफल लौटाने का तरीका।
        """
        return a * b

class Derived(Addition, Multiplication):  # Derived क्लास Addition और Multiplication दोनों से इनहेरिट करती है
    def Divide(self, a, b):
        """
        दो संख्याओं का भागफल लौटाने का तरीका।
        """
        return a / b

# Derived क्लास का एक उदाहरण बनाएं
derived_obj = Derived()
# Addition, Multiplication और Derived क्लास की विधियों को कॉल करें
print(derived_obj.sum(10, 20))        # आउटपुट: 30
print(derived_obj.multiply(10, 20))   # आउटपुट: 200
print(derived_obj.Divide(10, 20))     # आउटपुट: 0.5
```

### व्याख्या:

1. **बेस क्लासेस**:
   - **`Addition`**: इसमें एक विधि `sum()` है, जो दो संख्याओं का योग लौटाती है।
   - **`Multiplication`**: इसमें एक विधि `multiply()` है, जो दो संख्याओं का गुणनफल लौटाती है।

2. **डेरिव्ड क्लास (`Derived`)**:
   - यह `Addition` और `Multiplication` दोनों से इनहेरिट करती है।
   - इसमें एक नई विधि `Divide()` है, जो दो संख्याओं का भागफल लौटाती है।

3. **मल्टिपल इनहेरिटेंस**:
   - `Derived` क्लास दोनों `Addition` और `Multiplication` की विधियों को इनहेरिट करती है।
   - यह `Derived` को अपने पैरेंट क्लासेस की विधियों के साथ-साथ अपनी नई विधियों का उपयोग करने की अनुमति देता है।

### मुख्य बातें:
- **मल्टिपल इनहेरिटेंस**: एक क्लास एक से अधिक बेस क्लासेस से इनहेरिट कर सकती है और उनकी कार्यक्षमताओं को जोड़ सकती है।
- **विधि पहुंच**: `Derived` क्लास `Addition` से `sum()` और `Multiplication` से `multiply()` विधियों को कॉल कर सकती है और साथ ही अपनी `Divide()` विधि का भी उपयोग कर सकती है।

इस उदाहरण से यह दिखाया गया है कि मल्टिपल इनहेरिटेंस कैसे एक डेरिव्ड क्लास में कई बेस क्लासेस की विशेषताओं को जोड़ने की अनुमति देता है।
