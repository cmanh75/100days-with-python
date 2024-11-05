import pandas
import random
import smtplib
from datetime import datetime

with open("account.txt", "r") as file:
    account_data = file.readlines()

my_email = account_data[0]
my_password = account_data[1]


today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    random_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_file, "r") as file:
        contents = file.read()
    contents = contents.replace("[NAME]", birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
