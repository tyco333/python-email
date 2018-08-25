import smtplib
import time
#Replace emailuser with your gmail username, emailpass with your gmail password, and emaildest with the email adress of the destination
def sendemail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("emailuser", "emailpass")
	server.sendmail("emailuser", "emaildest", msg)
	server.quit()
sendemail("a test")
