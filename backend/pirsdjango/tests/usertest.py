import requests
import json
url_register="http://127.0.0.1:8000/users/register/"
url_login="http://127.0.0.1:8000/users/login/"
url_profile="http://127.0.0.1:8000/userprofile/profile/"
auth_token=""
data={
    "username":"test212",
    "password":"testpassword",
    "email": "testmail@testmail.com"
}
print("registering")
response=requests.post(url_register,data=data)
print(response.json())
auth_token=response.json()['token']

print("logging in")
response=requests.post(url_login,data=data,headers={'Authorization': 'Token '+auth_token})
print(response.json())

print("getting user profile")
response= requests.get(url_profile,headers={'Authorization': 'Token '+auth_token})
print(response)
