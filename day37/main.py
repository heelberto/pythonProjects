import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "heelberto"
token = "asdfjkl;asdfjkl;"

user_params = {
    "token": "asdfjkl;asdfjkl;",
    "username": "heelberto",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)

#graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

#graph_config = {
#    "id": "graph1",
#    "name": "Cycling Graph",
#    "unit": "Km",
#    "type": "float",
#    "color": "ajisai"
#}

headers = {
    "X-USER-TOKEN": token
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_post_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/20240623"



response = requests.delete(url=pixel_post_endpoint, headers=headers)

print(response.text)
