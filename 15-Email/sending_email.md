Here's the code with added comments and a brief explanation:

```python
import smtplib

# Create an SMTP client session object to connect to the Gmail SMTP server
connection = smtplib.SMTP('smtp.gmail.com', 587)

# Identify the client to the mail server
connection.ehlo()

# Start TLS (Transport Layer Security) for secure communication
connection.starttls()

# Log in to the Gmail account using the provided credentials
connection.login('jacksonbuddy17@gmail.com', 'sender_password')

# Send an email
# Parameters:
# - Sender's email address: 'jacksonbuddy17@gmail.com'
# - Recipient's email address: 'jacksonbuddy17@gmail.com'
# - Email message content:
#   - 'Subject : This is the Subject' sets the subject of the email
#   - '\n\n' adds a line break
#   - 'Hello User' is the body of the email
connection.sendmail('jacksonbuddy17@gmail.com', 'jacksonbuddy17@gmail.com', 'Subject : This is the Subject \n\n Hello User')

# Terminate the SMTP session
connection.quit()
```

### Brief Explanation:

1. **Import Module**:
   - `import smtplib`: Imports the `smtplib` module, which provides functions to send emails using the SMTP protocol.

2. **Create SMTP Connection**:
   - `connection = smtplib.SMTP('smtp.gmail.com', 587)`: Creates an SMTP client session object and connects to Gmail's SMTP server using port 587 (standard for TLS).

3. **Identify the Client**:
   - `connection.ehlo()`: Sends an EHLO command to the server to identify the client and get server capabilities.

4. **Start TLS**:
   - `connection.starttls()`: Upgrades the connection to a secure encrypted TLS connection to ensure secure communication.

5. **Log In**:
   - `connection.login('jacksonbuddy17@gmail.com', 'sender_password')`: Authenticates the user by logging into the Gmail account with the provided email address and password.

6. **Send Email**:
   - `connection.sendmail('jacksonbuddy17@gmail.com', 'jacksonbuddy17@gmail.com', 'Subject : This is the Subject \n\n Hello User')`: Sends an email where:
     - The first parameter is the sender's email address.
     - The second parameter is the recipient's email address.
     - The third parameter is the email content, which includes a subject line and a body.

7. **Terminate Session**:
   - `connection.quit()`: Closes the SMTP session, releasing the connection to the server.