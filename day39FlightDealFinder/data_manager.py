import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

SHEETY_ENDPOINT_GET = "https://api.sheety.co/b832d7a0c6d4e4ea174ebc2fa95d87af/copyOfFlightDeals/prices"
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/b832d7a0c6d4e4ea174ebc2fa95d87af/copyOfFlightDeals/prices/"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    """
    # get the initial blank data from the sheet and save it to a text file to save on the number of API requests
    def __init__(self):
        # saving initial blank sheet to a text file

        initial_blank_response = requests.get(url=SHEETY_ENDPOINT_GET)
        # check for an error and raise one in the event it occurs during the request
        initial_blank_response.raise_for_status()
        # save data in the Google sheet
        sheet_data = initial_blank_response.json()["prices"]
        with open(file="sheets_data.txt", mode="w") as file:
            file.write(str(sheet_data))
    """

    # now we need to read the data from the sheets_data.txt file
    def __init__(self):
        self.destination_data = {}
        self.username = os.environ.get("_SHEETY_USERNAME_")
        self.password = os.environ.get("_SHEETY_PASSWORD_")
        self.authorization = HTTPBasicAuth(username=self.username, password=self.password)
        print(self.username)


    def get_destination_data(self):
        # using the data from the 'sheets_data.txt' file instead of making a 'GET' request
        with open(file="sheets_data.txt", mode="r") as file:
            self.destination_data = file.read()
        return self.destination_data

    def update_destination_code(self, id_num, new_info):
        put_response = requests.put(url=f"{SHEETY_ENDPOINT_PUT}{id_num}", json=new_info)
        print(put_response.text)

