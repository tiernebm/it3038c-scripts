import json
import requests

r = requests.get('http://localhost:3000')

data=r.json()

print(data[0].get('name') + " = " + data[0].get('color'))
print(data[1].get('name') + " = " + data[1].get('color'))
print(data[2].get('name') + " = " + data[2].get('color'))
print(data[3].get('name') + " = " + data[3].get('color'))