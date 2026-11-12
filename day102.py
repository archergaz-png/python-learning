import requests


response = requests.post (
    "https://httpbin.org/post",

    json={"title": "Изучить HTTPS", "priority": 2},
    timeout=10,

)

response.raise_for_status()
print (response.url)
