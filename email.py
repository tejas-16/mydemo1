import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "tejasvinchurkar16@gmail.com"
receiver_email = "tejasvinchurkar.scoe.comp@gmail.com"
password = "password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Some Title'

body = 'Hello Team, Please help me with the sanity check.'

msg_content = MIMEText(body, 'plain', 'utf-8')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
