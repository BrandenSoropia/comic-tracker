
import smtplib
from socket import gaierror
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

SMTP_SERVER_URL = os.environ["SMTP_SERVER_URL"]
# For SSL. 1025 for localhost smtp debug server
SMTP_SERVER_PORT = os.environ["SMTP_SERVER_PORT"]
SMTP_SERVER_SENDER_USER = os.environ["SMTP_SERVER_SENDER_USER"]
SMTP_SERVER_SENDER_PASSWORD = os.environ["SMTP_SERVER_SENDER_PASSWORD"]

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender
message["To"] = receiver

# We assume that the image file is in the same directory that you run your Python script from
encoded = base64.b64encode(open("cat.jpg", "rb").read()).decode()

text = """Hi, Check out the new post on the Mailtrap blog: SMTP Server for Testing: Cloud-based or Local? https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/ Feel free to let us know what content would be useful for you!"""
html = f"""<html> <body> <p>Hi,<br> Check out the new post on the Mailtrap blog:</p> <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p> <p> Feel free to <strong>let us</strong> know what content would be useful for you! <img src="data:image/jpg;base64,{encoded}"> </p> </body> </html> """

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

try:
    # send your message with credentials specified above
    with smtplib.SMTP(SMTP_SERVER_URL, SMTP_SERVER_PORT) as server:
        server.login(SMTP_SERVER_SENDER_USER, SMTP_SERVER_SENDER_PASSWORD)
        server.sendmail(sender, receiver, message.as_string())

    # tell the script to report if your message was sent or which errors need to be fixed
    print('Sent')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
