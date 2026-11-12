n = int(input("\n Введите количество чисел \n")) # Ввод количества чисел

numbers = [] #создает пустой список

for _ in range(n): # прогоняет программу n раз: ввели число - добавили в список - посчитали  
    number = str(input("\n Введите число и нажмите ENTER \t")) # пользователь вводит последовательно числа
    numbers.append(number) # добавляет введенные числа в созданный пустой список

def count_short_words(numbers):

    copied_list = [] # создали новый пустой список copied_list

    count = 0 

    for number in numbers:

        if len(number) <= 3:

            count +=1

            copied_list.append(number)

    return len(copied_list)

print (count_short_words(numbers))



    