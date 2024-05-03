import requests
import os, json
os.system("clear")


def get_my_token(username="a", password="1"):
    url = "http://127.0.0.1:8000/api/token/"

    data = {"username": username, "password": password}

    responce = requests.post(url=url, data=data)

    if responce.status_code == 200:
       return responce.json()['access']
    
    else:
        return None


URL = "http://127.0.0.1:8000/api/brands/"

access = get_my_token()

token = {'Authorization': f'Bearer {access}'}

responce = requests.get(url=URL, headers=token)

print(access)
print()
print(responce.json())