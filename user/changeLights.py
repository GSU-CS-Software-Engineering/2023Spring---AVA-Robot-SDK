import requests
import json


def changeLights(duration,r,g,b):
    username = "team2"
    password = "team2now"

    payload = {
        "duration": duration,
        "all":{
        "r": r,
        "g": g,
        "b": b
        }
    }

    response = requests.post('https://jtektdev.ava8.net/api/htproxy/WebDrive/BA00140/robot/misc/lights',
                            auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        out = json.dumps(data, indent=4)
    else:
        out = ('Failed with code: ', response.status_code)

    return out

