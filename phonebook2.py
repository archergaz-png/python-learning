contacts = {}

def add():
    name = input("Введите имя: ")
    number = input ("Введите номер: ")
    exist = False 
    for key in contacts:
        if key == name:
            exist = True
            break
    if exist: #if name in print (4 in f)
        print("Контакт уже есть")
                 
    else:
        contacts[name] = number
    print ("Контакт добавлен")

def show():
    #for key, value in contacts:
        #print (f" *** {key}: - {value}")
    print(contacts)

# def show_one():
    #name = action.split(" ")[1]
    #number = contacts.get(name)
    #if number is None:
            #print ("Контакта не сущ")
    #if name in contacts:
        #print (contacts[name])
    #else:
        #print ("Контакта не сущ")

def delete():
    name = input("Введите имя контакта для удаления: ")
    if name in contacts:
        contacts.pop (name)
    else:
        print ("Контакта не сущ")

def edit():
    name = input("Введите имя контакта для редактирования: ")
    number = contacts.get(name)
    if name in contacts:
        new_name = input("Введите новое имя контакта: ")
        new_number = input ("Введите новый номер контакта: ")
        contacts.pop (name)
        contacts[new_name] = new_number

    else:
        print ("Контакта не сущ")

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
        add()

    if action == "show":
        show()

    #if action.startswith("show "):
        #show_one()

    if action == "del":
        delete()

    if action == "edit":
            edit()

print ("Спасибо за использование!")