import requests
import json

url = 'http://httpbin.org/post'

args = {'id' : '1','pass' : '123'}

# La cabecera introduce el token para reconocer la aplicación
cabecera = {'Content-Type' : 'application/json', 'Access-token': '123456'}

r = requests.post(url,data=json.dumps(args),headers=cabecera)

print(r.url)

if r.status_code == 200:
    print(r.content)
