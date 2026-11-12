secret_number = 7
attempts = 3

print("Угадайте число от 1 до 10.")
print(f"У вас {attempts} попытки.")

for attempt in range(attempts):
    guess = int(input("Ваша попытка: "))

    if guess == secret_number:
        print("Верно! Вы угадали число.")
        break
    else:
        remaining = attempts - attempt - 1
        if remaining > 0:
            print(f"Не угадали. Осталось попыток: {remaining}")
        else:
            print(f"Не угадали. Попытки закончились. Секретное число: {secret_number}")