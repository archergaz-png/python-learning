
class Iterator:

    def __init__(self):
        self.c=1

    def __next__(self):
        self.c = 0

class Iterable:

    def __iter__(self):
      
itr = iter ([])
a = next(itr)
itr = iter ([])
b = next(itr)
itr = iter ([])
c = next(itr)
itr = iter ([])
d = next(itr)