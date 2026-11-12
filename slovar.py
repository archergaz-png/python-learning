def send_email(email, text):
    print (f"Отправили {text} для {email}")

person = {
    "name": "Alla",
    "email": "a@email.com",
    "hobby": "drawing"
}

email = person.get["email"]

if email is None:
    print ("Нет мыла")

if email is not None:
    send_email (email, "text")

# a ="123"
# b = "123"
# print (id(a))
# print (a is b)

# person.setdefault()
