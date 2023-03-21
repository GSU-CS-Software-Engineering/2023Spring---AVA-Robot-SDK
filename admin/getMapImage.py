import requests
from PIL import Image
from io import BytesIO


def getMapImage():
    username = "team2"
    password = "team2now"

    response = requests.get('https://jtektdev.ava8.net/api/db/map/image?db=GSU_ERB_3rd_220916&mapId=1',
                            auth=(username, password))

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGBA')
        return img.show()
    else:
        out = ('Failed with code: ', response.status_code)

    return out

getMapImage()
