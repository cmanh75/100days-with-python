import requests
from datetime import datetime

with open("day37/token.txt", "r") as file:
    my_token = file.read()

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": my_token,
    "username": "cmanh75",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/cmanh75/graphs"
headers = {
    "X-USER-TOKEN": user_parameters["token"]
}
graph_parameters = {
    "id": "cmanh75",
    "name": "cmanh75's revenue",
    "unit": "string",
    "type": "int",
    "color": "momiji",
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now()
quantity = input("how much you earn today?")

pixel_endpoint = f"https://pixe.la/v1/users/cmanh75/graphs/cmanh75/{today.strftime("%Y%m%d")}"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}
response = requests.put(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)