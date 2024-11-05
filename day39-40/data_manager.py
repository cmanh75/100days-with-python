import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    def __init__(self):
        self.user = os.environ["sheety_username"]
        self.password = os.environ["sheety_password"]
        self._authorizations = HTTPBasicAuth(self.user, self.password)
        self.data = self.get_data()
        self.customer_data = self.get_customer_email()
    def get_data(self):
        response = requests.get(url=os.environ["sheety_price_endpoint"], auth=self._authorizations)
        data = response.json()
        print(data)
        # return data["prices"]
    def update_data(self):
        for row in self.data:
            update_row = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{os.environ["sheety_price_endpoint"]}/{row["id"]}", json=update_row, auth=self._authorizations)
            response.raise_for_status()
    def get_customer_email(self):
        response = requests.get(url=os.environ["sheety_user_endpoint"], auth=self._authorizations)
        response.raise_for_status()
        return response.json()