list = ["apple, 'orangr"]

list_len = len(list)

for i in range (3): # первые два числа через зап это диапазон, после запятой - шаг
    print (list(1, 3, 3))
    print (i, list[i])
for ind, element in enumerate (list, start=1):
    print (ind, element)
