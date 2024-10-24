# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
import json

city_list = []

data_manager = DataManager()

# get the string text from 'sheets_data.txt' and convert it to json format/ dictionary
# "data_manager.get_destination_data()" returns the string content in the .txt file
# ".repalce("'", '"') " replaces each occurence of a single quote to a double quote
data_string = data_manager.get_destination_data().replace("'", '"')

# convert the string to a list, each item in the list is a dictionary, it represents a city
sheet_data = json.loads(data_string)

flight_search_manager = FlightSearch()
flight_data_manager = FlightData(flight_search_manager.token)
notification_manager = NotificationManager()


for cur_city in sheet_data:
    # find cities whose 'iataCode' is empty
    if cur_city["iataCode"] == "":
        # use the code_lookup method of the flight_search_manager
        # which initially only returns a string 'TESTING', later the city
        # look up functionality will be implemented
        cur_city["iataCode"] = flight_search_manager.code_lookup(cur_city["city"])
        #print(city["iataCode"])

        # create the data that will occupy what we would like to replace
        # in this case we want to load what is in the city["iataCode"], since in the line prior is when we use our
        # 'code_lookup' method to update what the code should be.
        new_data = {
            "price": {
                "iataCode": cur_city["iataCode"]
            }
        }
            # use the 'update destination_code' method on the data manager to update the actual google sheet with the
            # correct destination code, initially only updates w/ the default 'TESTING
            # ** keep the line below commented out to keep from wasting API calls **
        #   data_manager.update_destination_code(city["id"], new_data)

    cur_city_lowest_price = float(cur_city["lowestPrice"])
    #print(f"The current Lowest price for a flight from LON to {cur_city["iataCode"]} : ${cur_city_lowest_price}")
    flight_data_list = flight_data_manager.find_cheapest_flight(destination_code=f"{cur_city["iataCode"]}")
    for flight in flight_data_list:
        if float(flight["price"]["grandTotal"]) < cur_city_lowest_price:
            print("!LOW PRICE ALERT!")
            print(f"Previous cost: ${cur_city_lowest_price}\nNew cost : ${flight["price"]["grandTotal"]}")
            print(f"savings ${float(cur_city_lowest_price) - float(flight["price"]["grandTotal"])}")
            print(f"Fly from {flight["itineraries"]["segments"]["departure"]["iataCode"]}")
#            notification_manager.send_notification(prev_low=cur_city_lowest_price, new_low=float(flight["price"]["grandTotal"]))
        #print(f"Grand total: ${flight["price"]["grandTotal"]}")
