#link of tutorial: https://www.youtube.com/watch?v=sXjpkcF7rPQ



import smtplib

sender_email= "diegopaladinoemfrc@gmail.com"
rec_email="diegopaladinofoto@gmail.com"
password=input(str("digite a senha: "))
message=" texto (0123456789) "

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print("Login succes")
server.sendmail(sender_email,rec_email,message)
print("Email has sent to",rec_email)

#Wasn't possible to send humbers and special caracters like " : " in the "message"