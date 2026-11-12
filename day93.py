def fib(limit):
    counter = 0 
    start, nex = 0, 1
    while counter < limit:
        yield start 
        counter +=1 
        first, nex = nex, first + nex

for el in fib(10):
   
    print(el)
