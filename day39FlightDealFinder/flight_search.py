import os
import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:
    def __init__(self):
        self.API_KEY = os.environ.get("_AMADEUS_API_KEY_")
        self.API_SECRET = os.environ.get("_AMADEUS_API_SECRET_")
        self.token = self.get_new_token()

    def get_new_token(self):
        """
        :return: the token to be used for further API calls
        """
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.API_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def code_lookup(self, city_name):
        """
        :param city_name: string in the format of 'paris', 'new york', 'istanbul'
        :return: the IATA code for the corresponding 'city_name'

        done with the use of AMADEUS' 'City Search' call, upon a successful call, the first response's IATA code is
        returned. A try block is used in the event of an index error or a key error, that would mean no airport was
        found
        """
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=header,
            params=query)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
