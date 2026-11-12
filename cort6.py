def introduce(name, age):
    print(f"{name}, {age} лет")

data = ["Мария", 30]
introduce(*data)

info = {"name": "Пётр", "age": 40}
introduce(**info)