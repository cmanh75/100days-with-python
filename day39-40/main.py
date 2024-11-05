from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
import time
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

notification = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()
time.sleep(3)
for data in data_manager.data:
    data["iataCode"] = flight_search.find_code(data["city"])
data_manager.update_data()
tomorrow = datetime.now() + timedelta(days=1)
email_list = [row["whatIsYourEmail?"] for row in data_manager.customer_data["users"]]
six_month_after = datetime.now() + timedelta(days=(3 * 60))
for destination in data_manager.data:
    flights = flight_search.check_flights("LON", destination["iataCode"], tomorrow, six_month_after, False)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"Getting flight for {destination["city"]}...")
    print(f"{destination["city"]} : £{cheapest_flight.price} with {cheapest_flight.stops}")
    time.sleep(3)
    if (cheapest_flight.price == "N/A"):
        continue
    message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
            f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "\
            f"with {cheapest_flight.stops} stop(s) "\
            f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
    for email in email_list:
        notification.send_mail(email, message)