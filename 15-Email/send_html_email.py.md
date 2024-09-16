```python
# Importing required libraries for sending emails
import smtplib, ssl  # 'smtplib' for email sending, 'ssl' for secure connections
from email.mime.text import MIMEText  # For email content in plain text and HTML formats
from email.mime.multipart import MIMEMultipart  # For handling emails with multiple content types (plain text and HTML)

# Defining the sender's and receiver's email addresses and the sender's password
sender_email = "mayank.sahu@gmail.com"  # The sender's email address
receiver_email = "abc@gmail.com"  # The receiver's email address
password = "PA$$12345"  # The sender's email account password

# Creating a MIMEMultipart message object to hold both plain text and HTML parts
message = MIMEMultipart("alternative")  # "alternative" means the email can have multiple formats (plain text and HTML)
message["Subject"] = "multipart test"  # Setting the subject of the email
message["From"] = sender_email  # Specifying the sender's email
message["To"] = receiver_email  # Specifying the receiver's email

# Creating the plain-text and HTML versions of the message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""  # Plain-text version of the email body

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
"""  # HTML version of the email body with a clickable link

# Creating MIMEText objects for both plain-text and HTML content
part1 = MIMEText(text, "plain")  # Plain-text part
part2 = MIMEText(html, "html")  # HTML part

# Attaching both the plain-text and HTML parts to the message object
# The email client will render the HTML part first if it supports it, otherwise the plain-text part
message.attach(part1)
message.attach(part2)

# Creating a secure SSL context to ensure a secure connection with the email server
context = ssl.create_default_context()

# Establishing a secure connection with Gmail's SMTP server using SSL
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    # Logging in to the sender's Gmail account
    server.login(sender_email, password)
    
    # Sending the email from the sender to the receiver
    server.sendmail(
        sender_email, receiver_email, message.as_string()  # Converting the message object to a string format
    )
```

### Explanation:

1. **Importing Libraries**:
   - `smtplib` is used to send emails using the Simple Mail Transfer Protocol (SMTP).
   - `ssl` ensures a secure connection to the email server.
   - `MIMEText` and `MIMEMultipart` handle different formats of email content (plain text, HTML).

2. **Email Setup**:
   - `sender_email` and `receiver_email` define the sender and receiver of the email.
   - `password` stores the sender's email password (for authentication during login).

3. **Message Construction**:
   - The `MIMEMultipart("alternative")` object is created to handle both plain text and HTML email formats.
   - The subject, sender, and receiver details are added to the `message`.

4. **Plain-Text and HTML Content**:
   - Two different formats of the email body are created: one as plain text (`text`) and another as HTML (`html`).

5. **Attaching Content**:
   - `MIMEText` objects are created for the plain-text and HTML versions.
   - Both parts are attached to the `message`. The email client will try to render the HTML part if supported, otherwise, it will render the plain-text part.

6. **Establishing a Secure Connection**:
   - A secure SSL context is created to ensure the email is sent securely.
   - The connection to Gmail's SMTP server is made using `SMTP_SSL` with the server address `smtp.gmail.com` and port `465`.

7. **Sending the Email**:
   - The sender logs in using their credentials.
   - The email is sent using the `sendmail()` method, which takes the sender's email, receiver's email, and the message content as a string.
