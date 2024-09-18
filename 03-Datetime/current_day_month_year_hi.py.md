
```python
from datetime import date, timedelta  # 'datetime' मॉड्यूल से 'date' और 'timedelta' को आयात करना

# आज की तारीख प्राप्त करना
currentStatus = date.today()

# वर्तमान दिन, महीना, और वर्ष प्रिंट करना
print("Current Date =", currentStatus.day)  # आउटपुट: वर्तमान दिन
print("Current Month =", currentStatus.month)  # आउटपुट: वर्तमान महीना
print("Current Year =", currentStatus.year)  # आउटपुट: वर्तमान वर्ष

# 'timedelta' का उपयोग करके कल की तारीख जानना (1 दिन जोड़ना)
tomorrowDate = currentStatus + timedelta(days=1)
print("Tomorrow Date =", tomorrowDate)  # आउटपुट: कल की तारीख

# कल की तारीख में एक और दिन जोड़कर परसों की तारीख जानना
aftertomorrow = tomorrowDate + timedelta(days=1)
print("After Tomorrow Date =", aftertomorrow)  # आउटपुट: परसों की तारीख

# 'timedelta' का उपयोग करके पिछली तारीख जानना (1 दिन घटाना)
previousDate = currentStatus - timedelta(days=1)
print("Previous Date =", previousDate)  # आउटपुट: पिछली तारीख
```

### स्पष्टीकरण:

1. **मॉड्यूल आयात करना**:
   - तारीखों के साथ काम करने के लिए `datetime` मॉड्यूल से `date` और `timedelta` क्लासेस को आयात किया जाता है।

2. **वर्तमान तारीख**:
   - `date.today()` वर्तमान तारीख प्राप्त करता है। दिन, महीना, और वर्ष को अलग-अलग एक्सेस करके प्रिंट किया जाता है।

3. **कल की तारीख**:
   - `timedelta(days=1)` का उपयोग करके वर्तमान तारीख में एक दिन जोड़कर कल की तारीख प्राप्त की जाती है।

4. **परसों की तारीख**:
   - कल की तारीख में एक और दिन जोड़कर परसों की तारीख प्राप्त की जाती है और प्रिंट की जाती है।

5. **पिछली तारीख**:
   - `timedelta(days=1)` का उपयोग करके एक दिन घटाकर पिछली तारीख प्राप्त की जाती है।

