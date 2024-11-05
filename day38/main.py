import requests 
from datetime import datetime
GENDER = "male"
WEIGHT = 70
HEIGHT = 183
AGE = 20

with open ("day38/api.txt", "r") as file:
    infor = file.readlines()

web_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_id = infor[0].strip()
app_key = infor[1].strip()
user_name = infor[3].strip()
password = infor[4].strip()
exercise = input("Tell me what exercise you did? ")

params = {
    "query": exercise,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key, 
}

response = requests.post(url=web_endpoint, json=params, headers=headers)
response.raise_for_status()
data = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

google_sheets_endpoint = infor[2].strip()
print(google_sheets_endpoint)
google_sheets_name = "sheet1"

for exercise in data["exercises"]:
    sheet_inputs = {
        google_sheets_name: {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(sheet_inputs)
    sheet_response = requests.post(url=google_sheets_endpoint, json=sheet_inputs, auth=(user_name, password))
    print(sheet_response.text)
