city = str(input("Введите название города"))

import requests

try: 
    response = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city, 
            "count": 1, 
            "language": "ru"},
    headers={"Accept": "application/json"},
    timeout=20
    ) 

    response.raise_for_status()
    data = response.json()

    print("Статус-код: ", response.status_code)
    print ("URL: ", response.url)

except requests.exceptions.Timeout:
    print("Тайм-аут сервера")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения")
except requests.exceptions.HTTPError:
    print("HTTP-ошибка:")
except requests.exceptions.JSONDecodeError:
    print("Сервер вернул не JSON")

results = data.get("results")

if results:
    city = results[0]
    
    response = requests.get(

        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": city["latitude"], 
            "longitude": city["longitude"], 
            "daily": "temperature_2m_max,temperature_2m_min",
            "forecast_days": 1,
            "timezone": "auto"
            },
        headers={"Accept": "application/json"},
        timeout=20
        ) 

    print("Найден город:", city["name"])
    print("Страна:", city.get("country"))
    print("Широта:", city["latitude"])
    print("Долгота:", city["longitude"])

    response.raise_for_status()
    data = response.json()
    daily = data.get("daily")
    dates = daily.get("time")
    max_temperatures = daily.get("temperature_2m_max")
    min_temperatures = daily.get("temperature_2m_min")

    print(f"Город: {city['name']}")
    print(f"Дата прогноза: {dates[0]}")
    print(f"Максимальная температура: {max_temperatures[0]} °C")
    print(f"Минимальная температура: {min_temperatures[0]} °C")

else:
    print("Город не найден.")