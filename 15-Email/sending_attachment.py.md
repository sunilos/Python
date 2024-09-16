```python
# Example of Sending Email With Attachment 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Importing necessary libraries for sending email with an attachment
import smtplib  # For creating an SMTP session to send the email
from email.mime.multipart import MIMEMultipart  # To create a multipart message (email with attachment)
from email.mime.text import MIMEText  # To attach the body of the email in plain text
from email.mime.base import MIMEBase  # To add any attachment file
from email import encoders  # For encoding the file in base64

# Sender's and Receiver's email addresses
fromaddr = "jacksonbuddy17@gmail.com"  # Sender's email address
toaddr = "jacksonbuddy17@gmail.com"  # Receiver's email address (could be different or same)

# Instance of MIMEMultipart - creating a message object that can contain attachments
msg = MIMEMultipart() 

# Storing the sender's email address
msg['From'] = fromaddr 

# Storing the receiver's email address
msg['To'] = toaddr 

# Storing the subject of the email
msg['Subject'] = "This is the Document Attached"

# String to store the body of the email
body = "Below is the Attachment"

# Attaching the body (plain text) to the email
msg.attach(MIMEText(body, 'plain')) 

# Opening the file to be sent as an attachment
filename = "File_name_with_extension"  # Name that will appear in the email attachment
attachment = open("Document.txt", "rb")  # File to be attached, opened in binary read mode

# Creating a MIMEBase instance for the file to be attached
p = MIMEBase('application', 'octet-stream')  # 'octet-stream' refers to any binary data

# Setting the payload of the attachment by reading the content of the file
p.set_payload((attachment).read()) 

# Encoding the attachment in base64 format for secure transfer
encoders.encode_base64(p) 

# Adding the header with the file name to the MIMEBase object
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# Attaching the MIMEBase (file attachment) to the message object
msg.attach(p) 

# Creating an SMTP session to connect to Gmail's SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server on port 587

# Starting TLS (Transport Layer Security) for securing the connection
s.starttls() 

# Authentication - logging into the sender's Gmail account
s.login(fromaddr, "sender_password")  # Replace "sender_password" with the actual password

# Converting the multipart message into a string format
text = msg.as_string() 

# Sending the email - from the sender to the receiver, including the attachment
s.sendmail(fromaddr, toaddr, text) 

# Terminating the SMTP session and closing the connection
s.quit() 
```

### Explanation:

1. **Imports**:
   - `smtplib`: Handles the email sending process through the SMTP protocol.
   - `MIMEMultipart`: Enables sending an email with multiple parts (text and attachments).
   - `MIMEText`: Attaches the plain text message to the email.
   - `MIMEBase`: Handles the attachment, converting it into a MIME-compliant format.
   - `encoders`: Encodes the attachment in base64 to ensure it's sent securely.

2. **Email Setup**:
   - `fromaddr` and `toaddr` store the sender's and receiver's email addresses, respectively.
   - `msg` is an instance of `MIMEMultipart` used to handle multiple parts (email text and attachments).
   - The email body is created using `MIMEText(body, 'plain')` and attached to the email.

3. **Attachment Setup**:
   - The file is opened in binary mode (`"rb"`), and `MIMEBase` is used to handle the file data.
   - The file data is encoded in base64 using `encoders.encode_base64()`, and a content disposition header is added to specify the file name in the attachment.

4. **SMTP Session**:
   - `smtplib.SMTP('smtp.gmail.com', 587)` creates a connection to Gmail's SMTP server.
   - TLS is started using `starttls()`, and the sender's Gmail account is authenticated with `login()`.
   - The multipart message is converted to a string using `msg.as_string()` and sent with `sendmail()`.

5. **Session Termination**:
   - `s.quit()` is called to close the SMTP session after sending the email.

Make sure to replace `sender_password` with the actual password, and the file `"Document.txt"` with the correct file path.
