import smtplib
import datetime as dt
import random

with open("day32/account.txt", "r") as file:
    account_data = file.readlines()

my_email = account_data[0]
my_password = account_data[1]

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("day32/quotes.txt", encoding="utf8") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n{quote}".encode("utf-8"))
    