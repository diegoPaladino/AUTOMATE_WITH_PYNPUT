#Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#tutorial link: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
#SENHA GERADA PELA SEGURANÇA DO GOOGLE: wvqgqcsdymjwsyhp

import smtplib

import config


def send_email(subject,msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS,config.PASSWORD)
		message = 'Subject:{}\n\n{}'.format(subject, msg)
		server.sendmail(config.EMAIL_ADDRESS, config.PASSWORD, message)
		server.quit()
		print("Sucess: Email sent!")
	except:
		print("Email failed to send.")

subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)

