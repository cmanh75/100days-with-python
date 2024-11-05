import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

with open("account.txt", "r") as file:
    account_data = file.readlines()


OWN_API_KEY = str(account_data[0].strip()) 
account_sid = account_data[1]
auth_token = account_data[2]

parameter = {
    "lat": 29.874910,
    "lon": 121.537498,
    "appid": OWN_API_KEY,
    "cnt": 4,
}

response = requests.get(url=OWN_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()
will_rain = False
for hour_data in data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        to='whatsapp:+84866334075'
    )
    print("Bring an umbrella")