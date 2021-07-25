import requests

headers= {}
headers['Authorization']= 'Bearer ENTER YOUR ACCESS TOKEN HERE'

r=requests.get('http://localhost:8000/todo/', headers=headers)

print(r.text)
