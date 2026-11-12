from itertools import chain

itr = Iterator()

for i in itr:
    print (i)

d = [1,2,3,4,5][2:4] #срез от 2 до 4

d = range (100)
sliced = islice(d,5,3,30)
print(sliced)
for i in sliced:
    print()


    