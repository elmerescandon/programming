import requests
import json

url = 'http://httpbin.org/post'

args = {'id' : '1', 'pass' : '123'}

# El tipo de contenido / cabecera
cabecera = {'Content-Type' : 'application/json'}

r = requests.post(url,data=json.dumps(args),headers=cabecera)

print(r.url)

if r.status_code == 200:
    print(r.content)
