यहाँ Python में ईमेल भेजने का एक उदाहरण है:

```python
# ईमेल भेजने के लिए आवश्यक लाइब्रेरीज़ को आयात करना
import smtplib, ssl  # 'smtplib' ईमेल भेजने के लिए, 'ssl' सुरक्षित कनेक्शन के लिए
from email.mime.text import MIMEText  # Plain text और HTML प्रारूप में ईमेल सामग्री के लिए
from email.mime.multipart import MIMEMultipart  # विभिन्न प्रकार की सामग्री (plain text और HTML) वाले ईमेल को संभालने के लिए

# भेजने वाले और प्राप्त करने वाले ईमेल पते और भेजने वाले का पासवर्ड परिभाषित करना
sender_email = "mayank.sahu@gmail.com"  # भेजने वाले का ईमेल पता
receiver_email = "abc@gmail.com"  # प्राप्त करने वाले का ईमेल पता
password = "PA$$12345"  # भेजने वाले के ईमेल खाते का पासवर्ड

# MIMEMultipart संदेश ऑब्जेक्ट बनाना जिसमें plain text और HTML दोनों भाग होंगे
message = MIMEMultipart("alternative")  # "alternative" का मतलब है कि ईमेल में कई प्रारूप हो सकते हैं (plain text और HTML)
message["Subject"] = "multipart test"  # ईमेल का विषय सेट करना
message["From"] = sender_email  # भेजने वाले का ईमेल निर्दिष्ट करना
message["To"] = receiver_email  # प्राप्त करने वाले का ईमेल निर्दिष्ट करना

# संदेश के plain-text और HTML संस्करण बनाना
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""  # ईमेल बॉडी का plain-text संस्करण

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""  # HTML संस्करण जिसमें क्लिक करने योग्य लिंक है

# दोनों plain-text और HTML सामग्री के लिए MIMEText ऑब्जेक्ट बनाना
part1 = MIMEText(text, "plain")  # Plain-text भाग
part2 = MIMEText(html, "html")  # HTML भाग

# संदेश ऑब्जेक्ट में दोनों plain-text और HTML भागों को जोड़ना
# ईमेल क्लाइंट HTML भाग को पहले रेंडर करेगा यदि यह समर्थित हो, अन्यथा plain-text भाग को रेंडर करेगा
message.attach(part1)
message.attach(part2)

# एक सुरक्षित SSL कनेक्शन बनाने के लिए SSL संदर्भ बनाना
context = ssl.create_default_context()

# Gmail के SMTP सर्वर के साथ SSL का उपयोग करके सुरक्षित कनेक्शन स्थापित करना
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    # भेजने वाले के Gmail खाते में लॉगिन करना
    server.login(sender_email, password)
    
    # भेजने वाले से प्राप्त करने वाले को ईमेल भेजना
    server.sendmail(
        sender_email, receiver_email, message.as_string()  # संदेश ऑब्जेक्ट को स्ट्रिंग प्रारूप में बदलना
    )
```

### व्याख्या:

1. **लाइब्रेरीज़ का आयात**:
   - `smtplib` ईमेल भेजने के लिए उपयोग की जाती है।
   - `ssl` ईमेल सर्वर से सुरक्षित कनेक्शन सुनिश्चित करता है।
   - `MIMEText` और `MIMEMultipart` विभिन्न ईमेल सामग्री प्रारूपों (plain text, HTML) को संभालते हैं।

2. **ईमेल सेटअप**:
   - `sender_email` और `receiver_email` भेजने वाले और प्राप्त करने वाले ईमेल को परिभाषित करते हैं।
   - `password` भेजने वाले के ईमेल अकाउंट का पासवर्ड (लॉगिन के दौरान प्रमाणीकरण के लिए) होता है।

3. **संदेश निर्माण**:
   - `MIMEMultipart("alternative")` ऑब्जेक्ट को plain text और HTML ईमेल प्रारूपों को संभालने के लिए बनाया जाता है।
   - संदेश का विषय, भेजने वाला और प्राप्त करने वाला विवरण `message` में जोड़ा जाता है।

4. **Plain-Text और HTML सामग्री**:
   - ईमेल बॉडी के दो विभिन्न प्रारूप बनाए जाते हैं: एक plain text (`text`) और दूसरा HTML (`html`)।

5. **सामग्री जोड़ना**:
   - `MIMEText` ऑब्जेक्ट्स plain-text और HTML संस्करणों के लिए बनाए जाते हैं।
   - दोनों भाग `message` में जोड़े जाते हैं। ईमेल क्लाइंट HTML भाग को पहले रेंडर करेगा यदि समर्थित हो, अन्यथा plain-text भाग को रेंडर करेगा।

6. **सुरक्षित कनेक्शन स्थापित करना**:
   - एक सुरक्षित SSL संदर्भ बनाया जाता है ताकि ईमेल सुरक्षित रूप से भेजा जा सके।
   - Gmail के SMTP सर्वर के साथ SSL का उपयोग करके कनेक्शन स्थापित किया जाता है (`smtp.gmail.com` और पोर्ट `465` के साथ)।

7. **ईमेल भेजना**:
   - भेजने वाला अपने क्रेडेंशियल्स का उपयोग करके लॉगिन करता है।
   - ईमेल `sendmail()` मेथड का उपयोग करके भेजा जाता है, जो भेजने वाले का ईमेल, प्राप्त करने वाले का ईमेल, और संदेश की सामग्री को स्ट्रिंग प्रारूप में लेता है।
