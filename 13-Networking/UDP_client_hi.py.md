यहाँ एक कोड स्निपेट है जो Python में एक UDP क्लाइंट सॉकेट बनाने का उदाहरण देता है:

```python
# UDP क्लाइंट सॉकेट बनाने का उदाहरण
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket

# एक UDP सॉकेट बनाएँ
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# कनेक्ट करने के लिए होस्ट और पोर्ट को परिभाषित करें
udp_host = socket.gethostname()    # होस्ट IP
udp_port = 12345                  # निर्दिष्ट पोर्ट जिसे कनेक्ट करना है

# सर्वर को भेजे जाने वाले संदेश
msg = b'Hello Server!'

print("UDP लक्षित IP:", udp_host)
print("UDP लक्षित पोर्ट:", udp_port)

# सर्वर को संदेश भेजें
sock.sendto(msg, (udp_host, udp_port))
```

### मुख्य बिंदु:
- **सॉकेट निर्माण**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` एक UDP सॉकेट बनाता है। `AF_INET` IPv4 पते के लिए प्रयोग किया जाता है, और `SOCK_DGRAM` UDP के लिए सॉकेट प्रकार को निर्दिष्ट करता है।
- **संदेश तैयारी**: संदेश को बाइट ऑब्जेक्ट (`b'Hello Server!'`) के रूप में बनाया गया है।
- **डेटा भेजना**: `sock.sendto(msg, (udp_host, udp_port))` संदेश को निर्दिष्ट होस्ट और पोर्ट पर भेजता है।

यह UDP क्लाइंट निर्दिष्ट होस्ट और पोर्ट पर एक संदेश भेजेगा। UDP कनेक्शनलेस होता है, इसलिए डेटा भेजने से पहले कनेक्शन स्थापित करने की आवश्यकता नहीं होती।
