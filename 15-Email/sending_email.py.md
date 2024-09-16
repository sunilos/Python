```python
# Example of Sending Email by Gmail Account
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Importing the smtplib library to handle email sending via SMTP
import smtplib

# Creating an SMTP connection to Gmail's SMTP server (smtp.gmail.com) on port 587 (for TLS)
connection = smtplib.SMTP('smtp.gmail.com', 587)

# Identifying the client to the SMTP server (EHLO or HELO command)
connection.ehlo()

# Starting TLS (Transport Layer Security) for secure communication with the server
connection.starttls()

# Logging into the Gmail account using the sender's email and password
connection.login('jacksonbuddy17@gmail.com', 'sender_password')  # Replace 'sender_password' with the actual password

# Sending the email using the 'sendmail' method
# Parameters: sender's email, receiver's email, and the content of the email (including subject and body)
connection.sendmail('jacksonbuddy17@gmail.com', 'jacksonbuddy17@gmail.com', 'Subject: This is the Subject\n\nHello User')

# Quitting and closing the connection to the SMTP server
connection.quit()
```

### Explanation:

1. **Importing Library**:
   - `smtplib`: Used for sending emails using the Simple Mail Transfer Protocol (SMTP).

2. **Establishing a Connection**:
   - `smtplib.SMTP('smtp.gmail.com', 587)`: Establishes a connection to Gmail’s SMTP server over port 587, which is used for encrypted email sending using TLS.

3. **EHLO Command**:
   - `ehlo()`: Sends an Extended Hello (EHLO) command to the SMTP server to identify the client and indicate readiness for further commands.

4. **Starting TLS**:
   - `starttls()`: Initiates the TLS encryption, which secures the email communication between the client and the server.

5. **Logging In**:
   - `login('email', 'password')`: Authenticates the sender using the provided email and password. Replace `sender_password` with the actual password for the Gmail account.

6. **Sending the Email**:
   - `sendmail('from', 'to', 'message')`: Sends an email from the sender to the recipient.
     - `'Subject: This is the Subject\n\nHello User'`: The message string contains the subject (`'Subject: This is the Subject'`) followed by two newlines (`\n\n`) and then the body (`'Hello User'`).

7. **Closing the Connection**:
   - `quit()`: Ends the SMTP session and closes the connection to the Gmail server.

### Notes:
- Replace the sender's email and password with actual credentials.
- Ensure that the Gmail account allows "less secure apps" or has OAuth-based authentication configured if necessary.
