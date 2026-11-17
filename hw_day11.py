currency_1 = (input("Введите код исходной валюты ")).upper()
currency_2 = (input("Введите код целевой валюты ")).upper()
summa = float(input("Введите сумму "))

import requests

response = requests.get ("https://api.frankfurter.dev/v2/rates",
                         params= {"base": currency_1, "quotes": currency_2},
                         headers={"Accept": "application/json"},
                         timeout=20)

response.raise_for_status()
data = response.json()

print("Статус-код: ", response.status_code)
print ([data])

for item in data:
    print ("Дата запроса: ",item['date'])
    print ("Исходная валюта: ",item['base'])
    print ("Целевая валюта: ",item['quote'])
    print ("Курс: ",item['rate'])
    print ("Результат: ", (summa*item['rate']))