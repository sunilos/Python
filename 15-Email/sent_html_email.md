Here's the code with added comments and a brief explanation:

```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the sender's and receiver's email addresses
sender_email = "mayank.sahu@gmail.com"
receiver_email = "abc@gmail.com"
# Define the password for the sender's email account
password = "PA$$12345"

# Create a MIMEMultipart object to handle both plain-text and HTML versions of the email
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"  # Subject line of the email
message["From"] = sender_email          # Sender's email address
message["To"] = receiver_email          # Receiver's email address

# Create the plain-text version of the email
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

# Create the HTML version of the email
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
"""

# Convert the plain-text and HTML strings into MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Attach the plain-text and HTML parts to the MIMEMultipart message
# The email client will try to render the last part first (HTML in this case)
message.attach(part1)
message.attach(part2)

# Create a secure SSL context for connecting to the email server
context = ssl.create_default_context()

# Connect to the email server using SMTP over SSL
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    # Log in to the email account using the provided credentials
    server.login(sender_email, password)
    # Send the email
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
```

### Brief Explanation:

1. **Import Modules**:
   - `import smtplib, ssl`: Imports the necessary libraries for sending emails securely.
   - `from email.mime.text import MIMEText`: Imports the `MIMEText` class to handle plain-text and HTML email content.
   - `from email.mime.multipart import MIMEMultipart`: Imports the `MIMEMultipart` class to combine different parts (plain-text and HTML) into one email.

2. **Email Setup**:
   - `sender_email`, `receiver_email`, and `password` define the sender's email address, receiver's email address, and the sender's email password respectively.
   - `message = MIMEMultipart("alternative")` creates a `MIMEMultipart` object to handle different types of email content.

3. **Email Content**:
   - `text` and `html` define the plain-text and HTML versions of the email content.
   - `part1` and `part2` convert the `text` and `html` strings into `MIMEText` objects.

4. **Attach Content**:
   - `message.attach(part1)` and `message.attach(part2)` add the plain-text and HTML parts to the email message.

5. **Send Email**:
   - `context = ssl.create_default_context()` creates a secure SSL context.
   - `with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server` establishes a secure connection to the Gmail SMTP server.
   - `server.login(sender_email, password)` logs in to the email account.
   - `server.sendmail(sender_email, receiver_email, message.as_string())` sends the email to the recipient.