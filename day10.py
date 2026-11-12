import requests


response = requests.get (
    "https://jsonplaceholder.typicode.com/posts"
)

if response.status_code == 200:
    try:
        posts = response.json()[:3]
    except:
        print ("в ответе не json")
    else: 
        for post in posts:
            print("название поста: ", post["title"])
            print ("текст поста: ", post["body"])
            print (">>>>>")
else: 
    print ("Ответ не успешный", response.status_code)





