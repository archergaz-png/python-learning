a = int(input("Введите первое число "))
sign = str(input("Введите знак арифметической операции "))
b = int(input("Введите второе число "))
if sign == "+":
    sum = (a + b) 
    print ("Ответ: "+ str(sum))
elif sign == "-":
    razn = (a - b)
    print ("Ответ: "+ str(razn))
elif sign == "*":
    umno = (a * b)
    print("Ответ: "+ str(umno))
elif sign == "/":
    deli = (a / b)
    print("Ответ: "+ str(deli))