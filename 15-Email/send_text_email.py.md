```python
# Importing the necessary libraries
import smtplib  # smtplib is used for sending emails via the Simple Mail Transfer Protocol (SMTP)
import traceback  # traceback is used for printing error messages when exceptions occur

# Sender's Gmail credentials
gmail_user = 'you@gmail.com'  # Replace this with the sender's Gmail address
gmail_password = 'P@ssword!'  # Replace this with the sender's Gmail password

# Setting up the email details
sent_from = gmail_user  # The email is being sent from this address (same as the sender's Gmail)
to = ['me@gmail.com', 'bill@gmail.com']  # List of recipient email addresses
subject = 'This is my first Python Message'  # Subject of the email
body = 'Hi, What is going on'  # Body content of the email

# Trying to send the email using Gmail's SMTP server
try:
    # Establish a secure connection with Gmail's SMTP server using SSL on port 465
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    # Identifying with the server (EHLO is Extended HELO, a protocol command used to start the email session)
    server.ehlo()
    
    # Logging into the sender's Gmail account using the provided credentials
    server.login(gmail_user, gmail_password)
    
    # Sending the email using the server's sendmail() method
    # The parameters are: sender's email, recipient list, and the body of the email
    server.sendmail(sent_from, to, body)
    
    # Closing the connection with the server
    server.close()
    
    # If the email is sent successfully, print this message
    print('Email sent!')

# If an error occurs, it will be caught and the traceback (error message) will be printed
except:
    traceback.print_exc()  # Print the full stack trace of the error
```

### Explanation:

1. **Importing Libraries**:
   - `smtplib` allows us to connect to an email server to send emails.
   - `traceback` is imported to handle exceptions by printing detailed error messages.

2. **Email Credentials**:
   - `gmail_user` and `gmail_password` hold the sender's Gmail login details.
   - These will be used to authenticate the Gmail account when sending the email.

3. **Email Setup**:
   - `sent_from`: The email address of the sender (same as `gmail_user`).
   - `to`: A list of recipients (you can add multiple recipients here).
   - `subject` and `body`: These define the email's subject line and body content, respectively.

4. **Try Block**:
   - **Establishing Connection**: 
     - `SMTP_SSL` is used to establish a secure SSL connection to Gmail's SMTP server on port 465.
   - **EHLO Command**: 
     - `ehlo()` is sent to the server to identify the client and set up the session.
   - **Logging In**: 
     - `server.login()` is used to log in to the Gmail account using the credentials (`gmail_user` and `gmail_password`).
   - **Sending the Email**: 
     - `sendmail()` is used to send the email. The function takes three arguments: the sender's email, the recipient list, and the body of the email.
   - **Closing the Connection**: 
     - After sending the email, `server.close()` closes the connection to the server.
   - **Success Message**: 
     - If the email is sent successfully, `"Email sent!"` is printed.

5. **Except Block**:
   - If an error occurs during any part of the process, the `except` block will catch it and print the full error traceback using `traceback.print_exc()`, allowing you to troubleshoot the issue.
