h = int(input("Введите высоту: "))
line = "*"
for i in range(1, h+1):
    for j in range (i):  
        print ()
    print(i,j, line * (j+1))

