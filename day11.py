import requests
import os
import json

from dotenv import load_dotenv
load_dotenv()

#gh_token=os.getenv("GH_TOKEN")
#print ( os.getenv("TERM"))
gh_token = os.getenv("GH_TOKEN")
base_url = "https://api.github.com"
gh_username = "octocat"

response = requests.get (

f"{base_url}/users/{gh_username}"

)

data = response.json()

print(data ["avatar_url"])
print(data ["html_url"])
#print(data ["public_repos"])

response = requests.get(

    f"{base_url}/users/{gh_username}/repos?per_page=3&page=2",

    params={"per_page": 5},
    headers={"Accept": "application/vnd.github+json"},
    timeout=10
)

data = response.json()

print(f"Репозитории - {gh_username}")
for repo in data:
    print(f"{repo['name']}, количество форков - {repo['forks']}, следят - {repo['watchers']} ")

try:
    response = requests.get(
    f"{base_url}/user",
    headers={
        "Authorization": f"Bearer {gh_token}"
    }
)

except requests.exceptions.Timeout:
    print("Тайм-аут сервера")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения")
except requests.exceptions.HTTPError:
    print("HTTP-ошибка:")
except requests.exceptions.JSONDecodeError:
    print("Сервер вернул не JSON")

response.raise_for_status()
data = response.json()

print(data["login"], data["id"])

dict_data = {"title": "Arthur", "body": "Vsem privet - eto obuchenir Python"}
data = json.dumps(dict_data)

response = requests.post (

f"{base_url}/repos/{gh_username}/hello-worId/issues", 
 headers={
        "Authorization": f"Bearer {gh_token}"
    },

    data=data

)

print("Статус-код: ", response.status_code)
print(response.json())
