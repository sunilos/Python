Here's the code with added comments and a brief explanation in points:

```python
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# Sender's email address
fromaddr = "jacksonbuddy17@gmail.com"
# Receiver's email address
toaddr = "jacksonbuddy17@gmail.com"

# Create an instance of MIMEMultipart to handle the email
msg = MIMEMultipart() 

# Store the sender's email address in the message
msg['From'] = fromaddr 

# Store the receiver's email address in the message
msg['To'] = toaddr 

# Store the subject of the email
msg['Subject'] = "This is the Document Attached"

# Body of the email
body = "Below is the Attachment"

# Attach the body of the email to the message
msg.attach(MIMEText(body, 'plain')) 

# Open the file to be sent as an attachment
filename = "File_name_with_extension"
attachment = open("Document.txt", "rb") 

# Create an instance of MIMEBase for the attachment
p = MIMEBase('application', 'octet-stream') 

# Read the file content and set it as the payload
p.set_payload((attachment).read()) 

# Encode the payload into base64 to make it suitable for email transmission
encoders.encode_base64(p) 

# Add header to the attachment with filename
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# Attach the MIMEBase instance to the MIMEMultipart message
msg.attach(p) 

# Create an SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587) 

# Start TLS for secure communication
s.starttls() 

# Authenticate with the sender's email credentials
s.login(fromaddr, "sender_password") 

# Convert the MIMEMultipart message into a string format
text = msg.as_string() 

# Send the email with attachment
s.sendmail(fromaddr, toaddr, text) 

# Terminate the SMTP session
s.quit() 
```

### Brief Explanation:

1. **Import Modules**:
   - `import smtplib`: Imports the SMTP library for sending emails.
   - `from email.mime.multipart import MIMEMultipart`: Imports the `MIMEMultipart` class for handling emails with multiple parts (e.g., text and attachments).
   - `from email.mime.text import MIMEText`: Imports the `MIMEText` class for handling email text.
   - `from email.mime.base import MIMEBase`: Imports the `MIMEBase` class for handling attachments.
   - `from email import encoders`: Imports encoders to encode the attachment in base64.

2. **Email Setup**:
   - `fromaddr` and `toaddr` are the email addresses of the sender and receiver.
   - `msg = MIMEMultipart()` creates a new email message object that can handle multiple parts (text and attachment).

3. **Set Email Headers**:
   - `msg['From']`, `msg['To']`, and `msg['Subject']` define the sender, receiver, and subject of the email, respectively.

4. **Email Body**:
   - `body` defines the text content of the email.
   - `msg.attach(MIMEText(body, 'plain'))` attaches the plain-text body to the email message.

5. **Attach File**:
   - `filename` specifies the name of the file to be attached.
   - `attachment` opens the file in binary read mode.
   - `p = MIMEBase('application', 'octet-stream')` creates a MIMEBase object for the file attachment.
   - `p.set_payload((attachment).read())` reads and sets the file content as the payload.
   - `encoders.encode_base64(p)` encodes the payload in base64.
   - `p.add_header('Content-Disposition', "attachment; filename= %s" % filename)` adds a header to indicate that this part is an attachment and specifies the filename.
   - `msg.attach(p)` attaches the file to the email message.

6. **Send Email**:
   - `s = smtplib.SMTP('smtp.gmail.com', 587)` creates an SMTP session with Gmail's SMTP server.
   - `s.starttls()` starts TLS (Transport Layer Security) to secure the connection.
   - `s.login(fromaddr, "sender_password")` logs in to the sender's email account with the provided password.
   - `text = msg.as_string()` converts the email message into a string format for sending.
   - `s.sendmail(fromaddr, toaddr, text)` sends the email.
   - `s.quit()` terminates the SMTP session.