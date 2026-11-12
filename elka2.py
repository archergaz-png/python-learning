h = int(input("Введите высоту: "))

for i in range(h):
    line = ''
    for j in range(i+1):
        line += '*'
    print(line)
