print("Привет! будешь пиво? y/n \n")
answer = str(input())
if answer == "y": 
    print ("\n \t А сколько тебе лет? \n")
    age = int(input())
    if age >= 18:
        print ("\n \t А деньги у тебя есть? y/n \n")
    else:
        print ("\n \t \t Тебе нельзя, ты еще мелкий! \n")
    money = str(input())
    if age >= 18 and money == "y":
        print("\n \t \t Покупай и пей на здоровье! \n")
    elif age >= 18 and money == "n":
        print ("\n \t \t Попроси денег в долг и приходи \n")
elif answer == "n":
    print ("\n \t Ну тогда пей кефир! \n")
    