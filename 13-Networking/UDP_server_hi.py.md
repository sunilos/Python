यहाँ एक कोड स्निपेट है जो Python में एक UDP सर्वर सॉकेट बनाने का उदाहरण देता है:

```python
# UDP सर्वर सॉकेट बनाने का उदाहरण
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

import socket

# एक UDP सॉकेट बनाएँ
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# बाइंड करने के लिए होस्ट और पोर्ट को परिभाषित करें
udp_host = socket.gethostname()    # होस्ट IP
udp_port = 12345                  # निर्दिष्ट पोर्ट जिसे सुनना है

# सॉकेट को होस्ट और पोर्ट पर बाइंड करें
sock.bind((udp_host, udp_port))

while True:
    print("क्लाइंट का इंतजार कर रहा है...")
    # क्लाइंट से डेटा प्राप्त करें
    data, addr = sock.recvfrom(1024)
    print("प्राप्त संदेश:", data.decode(), "से", addr)
```

### मुख्य बिंदु:
- **सॉकेट निर्माण**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` एक UDP सॉकेट बनाता है।
- **बाइंडिंग**: `sock.bind((udp_host, udp_port))` सॉकेट को निर्दिष्ट होस्ट और पोर्ट पर बाइंड करता है ताकि यह आने वाले संदेशों के लिए सुन सके।
- **डेटा प्राप्त करना**: `data, addr = sock.recvfrom(1024)` क्लाइंट से डेटा के लिए प्रतीक्षा करता है। यह मेथड डेटा और क्लाइंट के पते को लौटाता है।
- **डिकोडिंग**: `data.decode()` प्राप्त बाइट डेटा को डिस्प्ले के लिए एक स्ट्रिंग में परिवर्तित करता है।

यह UDP सर्वर लगातार आने वाले संदेशों के लिए सुनता है और प्राप्त संदेशों को भेजने वाले के पते के साथ प्रिंट करता है।
