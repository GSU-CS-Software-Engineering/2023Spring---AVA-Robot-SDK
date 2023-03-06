import requests
import json


def drive(translate, rotate, duration):
    username = "team2"
    password = "team2now"

    payload = {
        "translate": translate,
        "rotate": rotate,
        "duration":duration,
        "nudge": True
    }

    response = requests.post('https://jtektdev.ava8.net/api/htproxy/WebDrive/BA00140/robot/drive/velocity',
                            auth=(username, password),
                            json = payload)

    if response.status_code == 200:
        data = response.json()
        out = json.dumps(data, indent=4)
    else:
        out = ('Failed with code: ', response.status_code)

    return out

