import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email = os.environ["my_email"]
        self.my_pass = os.environ["my_app_pass"]
    def send_mail(self, email_list, email_body):
        connection = smtplib.SMTP("smtp.gmail.com")
        with connection:
            connection.starttls()
            connection.login(self.my_email, self.my_pass)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight\n\n{email_body}"
                )
