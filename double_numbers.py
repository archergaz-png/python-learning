n = int(input("\n Введите количество чисел \n")) # Ввод количества чисел

numbers = [] #создает пустой список

for _ in range(n): # прогоняет программу n раз
    number = int(input("\n Введите число и нажмите ENTER \t")) # пользователь вводит последовательно числа
    numbers.append(number) # добавляет введенные числа в созданный пустой список

def double_numbers(numbers): # объявили функцию
    
    copied_list = [] # создали новый пустой список copied_list

    for number in numbers: # для каждого числа из списка numbers 
        copied_list.append(number * 2) # добавить в список copied_list числа number из списка numbers умноженные на 2

    return copied_list # вернуть copied_list

result = double_numbers(numbers)

print(result)



     
    

        
      


