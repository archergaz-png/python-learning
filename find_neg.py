n = int(input("\n Введите количество чисел \n")) # Ввод количества чисел

numbers = [] #создает пустой список

for _ in range(n): # прогоняет программу n раз: ввели число - добавили в список - посчитали четные 
    number = int(input("\n Введите число и нажмите ENTER \t")) # пользователь вводит последовательно числа
    numbers.append(number) # добавляет введенные числа в созданный пустой список

def has_negative(numbers):

    count = 0 
   
    for number in numbers: 
        if number < 0:
         count +=1

        return count >0  

    else:
        return False

print (has_negative(numbers))




 


