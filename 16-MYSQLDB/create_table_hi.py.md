यहाँ एक कोड का उदाहरण है जो डेटाबेस में तालिकाएँ बनाने के लिए है, और इसके साथ एक संक्षिप्त व्याख्या दी गई है:

```python
# डेटाबेस में तालिका बनाने का उदाहरण

# Python फ़ंक्शंस और MySQL कनेक्टर का उपयोग करके तालिकाएँ बनाना

# mysql.connector मॉड्यूल से कनेक्शन ऑब्जेक्ट आयात करें
from mysql.connector import connection

# MySQL सर्वर से कनेक्शन स्थापित करें और डेटाबेस का चयन करें
conn = connection.MySQLConnection(
    user='root',            # MySQL यूज़रनेम
    password='root',        # MySQL पासवर्ड
    host='localhost',       # डेटाबेस सर्वर का पता (स्थानीय सर्वर के लिए localhost)
    charset='utf8',         # कनेक्शन के लिए कैरेक्टर सेट
    database='testdb'       # कनेक्ट करने के लिए डेटाबेस का नाम
)

# SQL क्वेरी को निष्पादित करने के लिए एक कर्सर ऑब्जेक्ट बनाएं
cursor = conn.cursor()

# 'student' नाम की तालिका बनाने के लिए SQL कमांड निष्पादित करें
cursor.execute("""
CREATE TABLE student (
    sid INT PRIMARY KEY AUTO_INCREMENT,     # 'sid' कॉलम: पूर्णांक, प्राथमिक कुंजी, स्वचालित रूप से वृद्धि
    StudentName VARCHAR(255),               # 'StudentName' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    RollNo VARCHAR(255)                     # 'RollNo' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
)
""")

# 'Registeration' नाम की तालिका बनाने के लिए SQL कमांड निष्पादित करें
cursor.execute("""
CREATE TABLE Registeration (
    regid INT PRIMARY KEY AUTO_INCREMENT,   # 'regid' कॉलम: पूर्णांक, प्राथमिक कुंजी, स्वचालित रूप से वृद्धि
    Firstname VARCHAR(255),                 # 'Firstname' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    LastName VARCHAR(255),                  # 'LastName' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    Email VARCHAR(255),                     # 'Email' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    Password VARCHAR(255),                  # 'Password' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    MobileNumber VARCHAR(255),              # 'MobileNumber' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
    address VARCHAR(255)                    # 'address' कॉलम: चर स्ट्रिंग जिसकी अधिकतम लंबाई 255 है
)
""")

# कर्सर और कनेक्शन को बंद करें
cursor.close()
conn.close()
```

### संक्षिप्त व्याख्या:

1. **मॉड्यूल आयात**:
   - `from mysql.connector import connection`: `mysql.connector` मॉड्यूल से `connection` ऑब्जेक्ट आयात करता है, जो MySQL डेटाबेस से कनेक्शन को प्रबंधित करता है।

2. **डेटाबेस कनेक्शन स्थापित करना**:
   - `conn = connection.MySQLConnection(...)`: निर्दिष्ट विवरणों के साथ MySQL सर्वर से कनेक्शन बनाता है।
     - `user='root'`: MySQL यूज़रनेम।
     - `password='root'`: MySQL पासवर्ड।
     - `host='localhost'`: MySQL सर्वर का होस्ट पता।
     - `charset='utf8'`: कनेक्शन के लिए कैरेक्टर सेट।
     - `database='testdb'`: कनेक्ट करने के लिए डेटाबेस का नाम।

3. **कर्सर ऑब्जेक्ट बनाना**:
   - `cursor = conn.cursor()`: SQL कमांड निष्पादित करने के लिए एक कर्सर ऑब्जेक्ट बनाता है।

4. **तालिकाएँ बनाना**:
   - `cursor.execute(...)`: SQL कमांड को निष्पादित करता है जो दो तालिकाएँ बनाता है:
     - `student`: इसमें छात्र ID (`sid`), नाम (`StudentName`), और रोल नंबर (`RollNo`) के लिए कॉलम होते हैं। `sid` कॉलम स्वचालित रूप से बढ़ने वाली प्राथमिक कुंजी है।
     - `Registeration`: इसमें पंजीकरण ID (`regid`), पहला नाम (`Firstname`), अंतिम नाम (`LastName`), ईमेल (`Email`), पासवर्ड (`Password`), मोबाइल नंबर (`MobileNumber`), और पता (`address`) के लिए कॉलम होते हैं। `regid` कॉलम स्वचालित रूप से बढ़ने वाली प्राथमिक कुंजी है।

5. **संसाधन बंद करना**:
   - `cursor.close()`: कर्सर ऑब्जेक्ट को बंद करता है ताकि डेटाबेस संसाधन मुक्त हो सकें।
   - `conn.close()`: MySQL सर्वर से कनेक्शन को बंद करता है।
