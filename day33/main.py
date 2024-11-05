import requests
from datetime import datetime
import smtplib

with open("account.txt", "r") as file:
    account_data = file.readlines()

my_email = account_data[0]
my_password = account_data[1]

MY_LAT = 21.027763 # Your latitude
MY_LONG = 105.834160 # Your longitude
def if_iss_up():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

if if_iss_up() and is_night():
    connect = smtplib.SMTP("smtp.gmail.com")
    connect.starttls()
    connect.login(my_email, my_password)
    connect.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject:Look up\n\n The ISS is above you in the sky."
    )

