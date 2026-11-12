import requests

try: 
    response = requests.get(
    "https://httpbin.org/get",
    params={"city": "Moscow", "days": 3},
    headers={"Accept": "application/json"},
    timeout=10

)   

    response.raise_for_status()
    data = response.json()

    print("Статус-код: ", response.status_code)
    print ("URL: ", response.url)
    print("Параметры: ", data["args"])

except requests.exceptions.Timeout:
    print("Тайм-аут сервера")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения")
except requests.exceptions.HTTPError:
    print("HTTP-ошибка:")
except requests.exceptions.JSONDecodeError:
    print("Сервер вернул не JSON")
