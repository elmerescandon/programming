import requests
import json

url = 'http://httpbin.org/post'

args = {
    'id' : '1',
    'pass' : '123'
}

r = requests.post(url,data=args)
# Ahora carga los valores de args en
# forms (contraintuitivo)

print(r.url)

if r.status_code == 200:
    print(r.content)
