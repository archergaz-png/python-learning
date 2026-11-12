contacts = {}


print ("q - выйти")
print ("add - добавить")
print ("del - удалить")
print ("show - показать")
print ("edit - изменить")

while True:
    print()
    action = input("Введите действие или q для выхода: ")
   
    if action == "q":
        break

    if action == "add":
        name = input("Введите имя контакта ") 
        number = input("Введите телефонный номер контакта ")
        contacts[name] = number 
        print ("Контакт успешно сохранен")
                
    if action == "show":
        print(contacts)

    if action == "del":
            name = input("Введите имя контакта для удаления: ")
            if name in contacts:
                contacts.pop (name)
            else:
                print ("Контакта не сущ")

# print(f.startswith(show ))
# name = action.split ("")[1]
# print(conyacy[name])
# if name in contacts
# print(контакт не сущ)
# print(f.split(" "))
