import requests
import json


def get_authorization():
    username = "team2"
    password = "team2now"

    response = requests.get('https://jtektdev.ava8.net/api/authenticated', auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        out = json.dumps(data, indent=4)
    else:
        out = ('Failed with code: ', response.status_code)

    return out


print(get_authorization())
