import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("API_TOKEN")

URL = "https://api.github.com/user"

URL_repos = "https://api.github.com/user/repos"


response = requests.get(
    URL, headers={"Authorization": "token {}".format(token)}
)

response_repos = requests.get(
    URL_repos, headers={"Authorization": "token {}".format(token)}
)

print(response.json()["login"])
print(response.json()["email"])

for item in response_repos.json():
    print(item["name"])

