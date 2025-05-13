import requests
import json

data = {"username": "paolo.losi@concern.net", "password": "palc7882"}

headers = {'content-type': 'application/json'}
json_data = json.dumps(data)

try:
    response = requests.post("https://api.mwater.co/v3/clients", data=json_data, headers=headers)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
