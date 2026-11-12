import requests

response = requests.post(
    "https://httpbin.org/post",
    json={"city": "Moscow", "days": 3},
    timeout = 10
)

response.raise_for_status()
data = response.json()

print(data["json"])