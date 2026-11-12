secret_number = 4
attempts = 3

print ("Введи число от 1 до 10 \n")
print (f"У тебя {attempts} попыток. Если облажаешься - ты лох \n" )

for attempt in range(attempts):
    guess = int(input("Твоя попытка: \n"))
    if guess == secret_number:
        print ("В точку! Возьми пирожок с полки\n")
        break
    else:
        while True:
            guess != secret_number and attempts > 0 and attempts != 1
            print ("Подумай еще \n")
            print (f"Попыток осталось - {attempts}")
            attempts = attempts - 1
            break
        if guess != secret_number and attempts == 1:
            print ("\n Осталась последняя попытка! Не облажайся!")
        if guess != secret_number and attempts == 0:
            print (f"\n Попытки закончились. Ты облажался. Секретное число: {secret_number} \n")


