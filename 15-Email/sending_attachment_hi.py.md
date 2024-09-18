यहाँ एक उदाहरण है जिसमें ईमेल के साथ एक अटैचमेंट भेजने की प्रक्रिया दिखाई गई है:

```python
# अटैचमेंट के साथ ईमेल भेजने के लिए आवश्यक लाइब्रेरीज़ को आयात करना
import smtplib  # SMTP प्रोटोकॉल के माध्यम से ईमेल भेजने के लिए
from email.mime.multipart import MIMEMultipart  # मल्टीपार्ट संदेश (ईमेल के साथ अटैचमेंट) बनाने के लिए
from email.mime.text import MIMEText  # ईमेल के बॉडी को plain text में अटैच करने के लिए
from email.mime.base import MIMEBase  # किसी भी अटैचमेंट फाइल को जोड़ने के लिए
from email import encoders  # फाइल को base64 में एन्कोड करने के लिए

# भेजने वाले और प्राप्तकर्ता के ईमेल पते
fromaddr = "jacksonbuddy17@gmail.com"  # भेजने वाले का ईमेल पता
toaddr = "jacksonbuddy17@gmail.com"  # प्राप्तकर्ता का ईमेल पता (वह अलग भी हो सकता है)

# MIMEMultipart का एक उदाहरण - एक संदेश ऑब्जेक्ट जो अटैचमेंट्स को संभाल सकता है
msg = MIMEMultipart() 

# भेजने वाले का ईमेल पता स्टोर करना
msg['From'] = fromaddr 

# प्राप्तकर्ता का ईमेल पता स्टोर करना
msg['To'] = toaddr 

# ईमेल का विषय स्टोर करना
msg['Subject'] = "This is the Document Attached"

# ईमेल के बॉडी को स्टोर करने के लिए एक स्ट्रिंग
body = "Below is the Attachment"

# बॉडी (plain text) को ईमेल में अटैच करना
msg.attach(MIMEText(body, 'plain')) 

# अटैचमेंट के लिए फाइल खोलना
filename = "File_name_with_extension"  # अटैचमेंट के रूप में दिखाई देने वाला नाम
attachment = open("Document.txt", "rb")  # अटैचमेंट फाइल, जो बाइनरी मोड में खोली जाती है

# MIMEBase इंस्टेंस बनाना अटैचमेंट के लिए
p = MIMEBase('application', 'octet-stream')  # 'octet-stream' किसी भी बाइनरी डेटा को संदर्भित करता है

# अटैचमेंट के payload को सेट करना, फाइल की सामग्री पढ़कर
p.set_payload((attachment).read()) 

# अटैचमेंट को base64 फॉर्मेट में एन्कोड करना
encoders.encode_base64(p) 

# MIMEBase ऑब्जेक्ट में फाइल नाम के साथ हेडर जोड़ना
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# MIMEBase (फाइल अटैचमेंट) को संदेश ऑब्जेक्ट में अटैच करना
msg.attach(p) 

# Gmail के SMTP सर्वर से कनेक्ट करने के लिए SMTP सत्र बनाना
s = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail के SMTP सर्वर पर पोर्ट 587 का उपयोग करना

# कनेक्शन को सुरक्षित करने के लिए TLS (Transport Layer Security) शुरू करना
s.starttls() 

# प्रमाणीकरण - भेजने वाले के Gmail खाते में लॉगिन करना
s.login(fromaddr, "sender_password")  # "sender_password" को वास्तविक पासवर्ड से बदलें

# मल्टीपार्ट संदेश को एक स्ट्रिंग फॉर्मेट में परिवर्तित करना
text = msg.as_string() 

# ईमेल भेजना - भेजने वाले से प्राप्तकर्ता तक, अटैचमेंट के साथ
s.sendmail(fromaddr, toaddr, text) 

# SMTP सत्र समाप्त करना और कनेक्शन बंद करना
s.quit() 
```

### व्याख्या:

1. **लाइब्रेरीज़ का आयात**:
   - `smtplib`: ईमेल भेजने के लिए SMTP प्रोटोकॉल का उपयोग करता है।
   - `MIMEMultipart`: मल्टीपार्ट ईमेल (टेक्स्ट और अटैचमेंट) भेजने की सुविधा देता है।
   - `MIMEText`: ईमेल के टेक्स्ट बॉडी को अटैच करने के लिए।
   - `MIMEBase`: अटैचमेंट को MIME-कॉम्प्लायंट फॉर्मेट में संभालता है।
   - `encoders`: अटैचमेंट को base64 में एन्कोड करता है ताकि यह सुरक्षित रूप से भेजा जा सके।

2. **ईमेल सेटअप**:
   - `fromaddr` और `toaddr` में भेजने वाले और प्राप्तकर्ता के ईमेल पते होते हैं।
   - `msg` एक `MIMEMultipart` ऑब्जेक्ट है जो मल्टीपार्ट ईमेल (टेक्स्ट और अटैचमेंट) को संभालता है।
   - ईमेल की बॉडी `MIMEText(body, 'plain')` के माध्यम से बनाई जाती है और ईमेल में अटैच की जाती है।

3. **अटैचमेंट सेटअप**:
   - फाइल को बाइनरी मोड (`"rb"`) में खोला जाता है और `MIMEBase` का उपयोग करके फाइल डेटा को हैंडल किया जाता है।
   - फाइल डेटा को base64 में एन्कोड किया जाता है और कंटेंट डिस्पोज़िशन हेडर जोड़कर अटैचमेंट के नाम को सेट किया जाता है।

4. **SMTP सत्र**:
   - `smtplib.SMTP('smtp.gmail.com', 587)` का उपयोग करके Gmail के SMTP सर्वर से कनेक्शन बनाया जाता है।
   - `starttls()` का उपयोग करके TLS शुरू किया जाता है और `login()` से Gmail खाते में लॉगिन किया जाता है।
   - मल्टीपार्ट संदेश को स्ट्रिंग में परिवर्तित करके `sendmail()` से भेजा जाता है।

5. **सत्र समाप्ति**:
   - ईमेल भेजने के बाद `s.quit()` से SMTP सत्र समाप्त किया जाता है और कनेक्शन बंद किया जाता है।

सुनिश्चित करें कि `sender_password` को वास्तविक पासवर्ड से बदलें और `"Document.txt"` को सही फाइल पथ से बदलें।
