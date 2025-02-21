import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("API_TOKEN")

URL = "https://api.github.com/user/repos"

# ip_response = requests.get(IP_URL).json()

# ip = ip_response["ip"]

# LOCATOR_URL = f"https://locator.api.maps.yandex.ru/v1/locate?apikey={token}"


response = requests.get(
    URL, headers={"Authorization": "token {}".format(token)}
)

for item in response.json():
    print(item["name"])

