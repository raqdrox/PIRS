import requests
import json

url_register="http://127.0.0.1:8000/apis/users/auth/register/"
url_login="http://127.0.0.1:8000/apis/users/auth/login/"
url_profile_view="http://127.0.0.1:8000/apis/users/profile/view/"
url_profile_update="http://127.0.0.1:8000/apis/users/profile/update/"
url_patient_create="http://127.0.0.1:8000/apis/patient/create/"
url_patient_getbyid="http://127.0.0.1:8000/apis/patient/get/"
url_patient_update="http://127.0.0.1:8000/apis/patient/update/"
url_patient_getbyname="http://127.0.0.1:8000/apis/patient/getbyname/"
url_patient_getbyfingerprint="http://127.0.0.1:8000/apis/patient/getbyfingerprint/"
auth_token="bd9d080da2c4ddbbcf5a321d2e914a629545deea"

data={
    "username":"usertest2",
    "password":"qwerty",
    "email":"test@test.com"
}

'''print("registering")
response=requests.post(url_register,data=data)
print(response.json())
auth_token=response.json()['token']

'''
print("logging in")
response=requests.post(url_login,data=data,headers={'Authorization': 'Token '+auth_token})
print(response.json())
auth_token=response.json()['token']

'''
print("update profile")
data={
    "name":"test",
    "address":"test address",
    "phone":"1234567890",
    "email":"test@test.com",
}
response=requests.post(url_profile_update,data=data,headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())
else:
    print(response)

print("view profile")
response = requests.get(url_profile_view,headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())
else:
    print(response)

print("create patient")
data={
    "id":6969,
    "name":"test2",
    "age":20,
    "dob":"2021-01-01",
    'email':'test@test.test',
    'phone':'1234567890',
    'address':'test address',
    'gender':'male',
    'medical_data':{
        'id':1,
        'blood_group':'A+',
        'diseases':'test disease',
        'allergies':'test allergy',
        'height':180,
        'weight':80,
    },
    'emergency_contact':{
        'id':1,
        'name':'test emergency contact',
        'phone':'1234567890',
    },
    'fingerprint_data':{
        'id':1,
        'fingerprint_data':'test fingerprint data',
        }

}

response=requests.post(url_patient_create,data=data,headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())


print("get patient by id")

response=requests.get(url_patient_getbyid+"1"+'/',headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())
else:
    print(response)
    '''
print("update patient")
data={
    "id":0,
    "name":"test2",
    "age":20,
    "dob":"2021-01-01",
    "gender":"Male",
    'email':'test@test.test',
    'phone':'1234567890',
    'address':'test address',
    "medical_data":{
        'blood_group':'A+',
        'diseases':'test disease',
        'allergies':'test allergy',
        'height':180,
        'weight':80,
    },
    "emergency_contact":{
        'name':'test emergency contact',
        'phone':'1234567890',
    },
    "fingerprint_data":{
        'fingerprint_data':'test fingerprint data',
        }

}
response=requests.post(url_patient_update+"213122"+'/',data=data,headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())
else:
    print(response.json())
'''
print("get patient by name")

response=requests.get(url_patient_getbyname+"asdasd"+'/',headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    (response.json())
else:
    print(response)


print("get patient by fingerprint")
data={'fingerprint_data':'adfg'}
response =requests.post(url_patient_getbyfingerprint,data=data,headers={'Authorization': 'Token '+auth_token})
if response.status_code==200:
    print(response.json())
else:
    print(response.json())

'''



