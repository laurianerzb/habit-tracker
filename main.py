import requests
from datetime import datetime as dt


pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_USERNAME = "PIXELA_USERNAME"
PIXELA_TOKEN = "PIXELA_TOKEN"
PIXELA_GRAPH_ID = "PIXELA_GRAPH_ID"
# create user parameters
users_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# create user
response = requests.post(pixela_endpoint, json=users_parameters)
response.raise_for_status()
print(response.json())

# create a graph for our username
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
# create graph parameters
graph_parameters = {
    "id": PIXELA_GRAPH_ID,
    "name": "reading tracker graph",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
# # create graph
graph_response = requests.post(url=graph_endpoint, headers=headers, json=graph_parameters)
graph_response.raise_for_status()
print(graph_response.json())

# post a pixel point
pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
today_date = dt(year=2023, month=8, day=20)
pixel_parameters = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": "15"
}
pixel_response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_parameters)
pixel_response.raise_for_status()
print(pixel_response.json())
# update a pixel point
pixel_endpoint_update = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/20230829"
pixel_parameters_update = {
    "quantity": "5.5"
}
pixel_response_u = requests.put(url=pixel_endpoint_update, headers=headers, json=pixel_parameters_update)
pixel_response_u.raise_for_status()
print(pixel_response_u.json())

# delete a pixel point
pixel_endpoint_delete = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/20230829"
pixel_response_d = requests.delete(url=pixel_endpoint_delete, headers=headers)
pixel_response_d.raise_for_status()
print(pixel_response_d.json())
