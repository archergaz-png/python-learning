from functools import reduce, partial, lru_cache
from time import sleep

def check_age(user, max_age):
    return user["age"] <= max_age

user1={"age":18}
user2={"age":35}

my_max=18

new_check_age = partial(check_age, my_max)


print(check_age(my_max, user1))

print(new_check_age(user1))


@lru_cache
def calc(a, b):
    sleep(2)
    return(a+b)

for i in [3,5,3,6,7,8,3]:
    print(calc(i,4))



