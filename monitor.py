import os
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"  # მაგალითად Gmail-ის SMTP
SMTP_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
        print("Email sent")

# გამოყენების მაგალითი
send_email("ახალი ფასდაკლება", "<b>მოგესალმები!</b><br>ახალი ფასდაკლება გამოვლინდა.")

