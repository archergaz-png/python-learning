

users = [ 
    {
        "name": a
        "age": 32
    }
]

super_adult_user = filter(lambda u: u["age"] >= 21, users)

for u in users:
    if u["age"] >= 21:
        print(u["name"])

