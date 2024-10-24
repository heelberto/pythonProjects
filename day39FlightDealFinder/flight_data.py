import os
import requests
import datetime

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHTS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, _token):
        self.API_KEY = os.environ.get("_AMADEUS_API_KEY_")
        self.API_SECRET = os.environ.get("_AMADEUS_API_SECRET_")
        self.token = _token
        self.price = 0
        self.departure_airport_code = "LON"

    def find_cheapest_flight(self, destination_code):
        """

        :param destination_code: string formatted in IATTA code format
        :return: a list of flights from the departure code: LON to the destination code
        """
        print(f"Looking for flights to {destination_code}...")

        # code to determine and format tomorrow's date as the departure date
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        date_1 = datetime.datetime.strptime(today, "%Y-%m-%d")
        # print(today)
        tomorrows_date = date_1 + datetime.timedelta(days=1)
        tomorrows_date = str(tomorrows_date).split(" ")[0]
        # print(tomorrows_date)

        header = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "originLocationCode": self.departure_airport_code,
            "destinationLocationCode": destination_code,
            "departureDate": tomorrows_date,
            "adults": 1,
            "currencyCode": "GBP",
            "nonStop": "true",
        }
        response = requests.get(
            url=FLIGHTS_ENDPOINT,
            headers=header,
            params=query)
        print(response.text)
        flight_data_list = response.json()["data"]
        return flight_data_list

