import smtplib, ssl
from email.message import EmailMessage
import settings

username = settings.EMAIL
password = settings.PASSWORD


def send_email(message, subject):
    host = "smtp-mail.outlook.com"
    port = 587

    receiver = "pena_matias@hotmail.com"

    message = message

    email = EmailMessage()
    email["From"] = username
    email["To"] = username
    email["Subject"] = subject
    email.set_content(message)

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, email.as_string())
        server.quit()


