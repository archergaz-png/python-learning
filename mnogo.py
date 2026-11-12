a = {1,2,3}
b = {3,4,5}
print (a & b)

a.add(4)
a.discard (2)

a = {1,2,3}
b = {3,4,5}
print (a | b & a)

def show_uni (*args):
    for a in set(args):
        print(a)

show_uni (123 ,456, 123)

df = dict(df=12) 
fg = {"df: 12"}
print (df)