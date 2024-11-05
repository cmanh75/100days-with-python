class FlightData:
    def __init__(self, price, origin, destination, out_date, return_date, stops):
        self.price = price
        self.origin = origin 
        self.destination = destination
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if data is None or ("data" not in data) or len(data["data"]) == 0:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    cheapest_flight = data["data"][0]
    for flight in data["data"]: 
        if float(flight["price"]["grandTotal"]) < float(cheapest_flight["price"]["grandTotal"]):
            cheapest_flight = flight
    lowest_price = float(cheapest_flight["price"]["grandTotal"])
    origin = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = cheapest_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    nr_stops = len(cheapest_flight["itineraries"][0]["segments"]) - 1
    return_date = cheapest_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    return FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)