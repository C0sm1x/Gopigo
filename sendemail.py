import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

emailAddress = open("email.txt", "r")
password = open("password.txt", "r")
toAddr = emailAddress.read()
fromAddr = emailAddress.read()
emailPassword = password.read()
msg = MIMEMultipart()
msg["From"] = fromAddr
msg["To"] = toAddr
msg["Subject"] = "Python Email"
body = "Here is your GoPiGo Picture!"
sendingMail = False
mailQuit = False

msg.attach(MIMEText(body, "plain"))

#filename = "picture`date +$y-%s`.jpg"
filename = "picture.jpg"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

email = smtplib.SMTP("smtp.gmail.com", 587)

email.starttls()

email.login(toAddr, emailPassword)

text = msg.as_string()

def sendpicture():
    sendingMail = True
    if sendingMail == True:
        email.sendmail(fromAddr, toAddr, text)
        print("Email sent!")

def sendemailQuit():
    email.quit()

    emailAddress.close()
    password.close()
    attachment.close()
    sendingMail = False



