
```python
# बाइनरी फ़ाइल की कॉपी करना
import shutil

source = "F:/baby.jpg"
target = "F:/boy.jpg"

shutil.copyfile(source, target)
print(source + " को " + target + " में कॉपी किया गया")
```

### व्याख्या:
- **`import shutil`**: `shutil` मॉड्यूल को आयात करता है, जो फ़ाइल ऑपरेशनों की एक श्रृंखला प्रदान करता है, जिसमें फ़ाइलों की कॉपी करना शामिल है।

- **`source` और `target`**: स्रोत फ़ाइल और लक्ष्य फ़ाइल के पथ को परिभाषित करते हैं जहां कॉपी सेव की जाएगी।

- **`shutil.copyfile(source, target)`**: स्रोत फ़ाइल की सामग्री को लक्ष्य फ़ाइल में कॉपी करता है। यदि लक्ष्य फ़ाइल पहले से मौजूद है, तो इसे ओवरराइट कर दिया जाएगा।

- **`print(source + " को " + target + " में कॉपी किया गया")`**: एक पुष्टि संदेश प्रिंट करता है, जो यह दर्शाता है कि फ़ाइल कॉपी ऑपरेशन पूरा हो गया है।
