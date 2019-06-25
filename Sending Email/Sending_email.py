# Example of Sending Email by Gmail Account
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import smtplib
connection = smtplib.SMTP('smtp.gmail.com' , 587)
connection.ehlo()
connection.starttls()
connection.login('jacksonbuddy17@gmail.com' , 'sender_password')
connection.sendmail('jacksonbuddy17@gmail.com' , 'jacksonbuddy17@gmail.com' , 'Subject : This is the Subject \n\n Hello User')
connection.quit()


