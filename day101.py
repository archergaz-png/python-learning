import requests


response = requests.get (
    "https://httpbin.org/get",
    params = {"city": "Moscow", "days": 3}, 
    timeout = 10,
)

print (response.url)