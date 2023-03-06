import requests
from PIL import Image
from io import BytesIO


def getCameraSnap():
    username = "team2"
    password = "team2now"

    response = requests.get('https://jtektdev.ava8.net/api/htproxy/WebDrive/BA00140/robot/camera/top',
                            auth=(username, password))

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGBA')
        return img.show()
    else:
        out = ('Failed with code: ', response.status_code)

    return out

getCameraSnap()
