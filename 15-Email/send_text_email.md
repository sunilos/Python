Here’s the code with comments added, followed by a brief explanation:

```python
import smtplib
import traceback

# Gmail credentials
gmail_user = 'you@gmail.com'  # Replace with your Gmail address
gmail_password = 'P@ssword!'  # Replace with your Gmail password

# Email details
sent_from = gmail_user
to = ['me@gmail.com', 'bill@gmail.com']  # List of recipient email addresses
subject = 'This is my first Python Message'
body = 'Hi, What is going on'

try:
    # Create an SMTP client session object using SSL for secure communication
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    # Identify the client to the server
    server.ehlo()
    
    # Log in to the Gmail account
    server.login(gmail_user, gmail_password)
    
    # Create the email headers
    email_message = f'Subject: {subject}\n\n{body}'
    
    # Send the email
    server.sendmail(sent_from, to, email_message)
    
    # Close the connection to the server
    server.close()
    
    print('Email sent!')

except Exception as e:
    # Print any exception that occurs during the process
    traceback.print_exc()
```

### Brief Explanation:

1. **Import Modules**:
   - `import smtplib`: Imports the `smtplib` module to handle email sending via SMTP.
   - `import traceback`: Imports the `traceback` module to provide detailed error information if an exception occurs.

2. **Set Up Email Credentials**:
   - `gmail_user`: Stores the sender's Gmail address.
   - `gmail_password`: Stores the password for the Gmail account.

3. **Define Email Details**:
   - `sent_from`: The sender's email address.
   - `to`: A list of recipient email addresses.
   - `subject`: The subject line of the email.
   - `body`: The body text of the email.

4. **Send Email in a `try` Block**:
   - `server = smtplib.SMTP_SSL('smtp.gmail.com', 465)`: Creates an SMTP client session object with SSL encryption for secure communication using Gmail’s SMTP server on port 465.
   - `server.ehlo()`: Identifies the client to the server.
   - `server.login(gmail_user, gmail_password)`: Logs in to the Gmail account using the provided credentials.
   - `email_message = f'Subject: {subject}\n\n{body}'`: Creates the email message with headers and body.
   - `server.sendmail(sent_from, to, email_message)`: Sends the email from the sender to the recipients with the constructed message.
   - `server.close()`: Closes the connection to the SMTP server.

5. **Handle Exceptions**:
   - `except Exception as e`: Catches any exceptions that occur during the email sending process.
   - `traceback.print_exc()`: Prints detailed error information to help debug issues.