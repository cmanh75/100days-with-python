import os
import requests
from dotenv import load_dotenv

load_dotenv()
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["amadeus_api_key"]
        self.secret = os.environ["amadeus_secret"]
        self.token = self.get_new_token()
    def get_new_token(self):
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": os.environ["amadeus_api_key"],
            "client_secret": os.environ["amadeus_secret"]
        }
        response = requests.post(url=token_endpoint, headers=headers, data=body)
        return response.json()["access_token"]
    def find_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(url=iata_endpoint, headers=headers, params=params)
        return response.json()["data"][0]["iataCode"]
    def check_flights(self, origin_code, destination_code, from_time, to_time, is_direct):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        print(is_direct)
        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=flight_endpoint, headers=headers, params=params)
        print(response.status_code)
        return response.json()