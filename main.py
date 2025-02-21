import requests
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

login = response.json()["login"]
email = response.json()["email"]

repos = response_repos.json()



with open("github_user_info.txt", "w") as file:
        file.write(f"Login: {login}\n")
        file.write(f"Email: {email}\n")
        file.write("Repositories:\n")
        for repo in repos:
            file.write(f"- {repo["name"]}\n")

print("Информация успешно сохранена в файл 'github_user_info.txt'.")

