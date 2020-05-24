#link of tutorial: https://www.youtube.com/watch?v=sXjpkcF7rPQ

#password='paladino804680'

import smtplib

sender_email= "diegopaladinoemfrc@gmail.com"
rec_email="diegopaladinofoto@gmail.com"
password='paladino804680'
#message=" texto 0123456789"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)

subject = 'texto subject'
body = 'ENTRADA: 12:00'

msg = f'Subject: {subject}\n\n{body}'

print("Login succes")
server.sendmail(sender_email,rec_email,msg)
print("Email has sent to",rec_email)

#Wasn't possible to send humbers and special caracters like " : " in the "message"