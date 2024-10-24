import requests
import datetime

APP_ID = "5662bbd8"
NUTRI_API_KEY = "9fcbc97532221df1ee0fe887c5bbf469"
NUTRI_NAT_LANG_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/b832d7a0c6d4e4ea174ebc2fa95d87af/copyOfMyWorkouts/workouts"

nat_lang_param = {
    "query": input("Tell me which exercise you did: ")
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': NUTRI_API_KEY
}

response = requests.post(url=NUTRI_NAT_LANG_ENDPOINT, json=nat_lang_param, headers=headers)
data = response.json()

# need a time in hh:mm:ss format
# formatted_time = now
# print(formatted_time)
# need the Type of Exercise
exercise_type = data["exercises"][0]["user_input"]
# need the duration in minutes
exercise_duration = data["exercises"][0]["duration_min"]
# and need the Calories
exercise_cal = data["exercises"][0]["nf_calories"]

for exercise in data["exercises"]:
    sheety_headers = {
        'workout': {
            'date': datetime.datetime.now().strftime("%d/%m/%Y"),
            'time': datetime.datetime.now().strftime("%H:%M:%S"),
            'exercise': exercise["user_input"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"]
        }
    }
    # test_response = requests.get(url=SHEETY_ENDPOINT, json={"Authorization": "Basic aGVlbGJlcnRvOnBhc3N3b3JkMzM="})

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_headers,auth=("heelberto", "password33"))
    print(sheety_response.text)

# print(f"{formatted_date}\t{formatted_time}\t{exercise_type}\t{exercise_duration}\t{exercise_cal}")
