# How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More
# tutorial link: https://www.youtube.com/watch?v=JRCJ6RtE3xU
#Joining the content of the some previous test (https://www.youtube.com/watch?v=sXjpkcF7rPQ) with this tutorial, was sucess!

import os
import smtplib

EMAIL_ADDRESS = os.environ.get('diegopaladinoemfrc@gmail.com')
EMAIL_PASSWORD = os.environ.get('paladino804680')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'texto subject'
    body = 'texto body'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,'diegopaladinofoto@gmail.com',msg)

#this was sucessed