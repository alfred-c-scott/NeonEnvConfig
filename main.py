#!/usr/bin/python3


import json


# installed
import requests


# local
from environment import env_vars


with open('payloads/create_location.json', 'r') as location_json:
    create_location = json.load(location_json)

# print(create_location)

response = requests.post(env_vars.ATWS_URL + '/locations', auth=(env_vars.ATWS_API_KEY, ''), json=create_location)


if response.status_code == 201:
    print("Success!")
    print(response.json())  # If the response is JSON
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)    # Print the response text for debugging