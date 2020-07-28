import requests
import json

# Post sirve para crear un parámetro dentro de la aplicación
url = 'http://httpbin.org/post'

args = {'id' : '1', 'pass' : '123'}
cabecera = {'Content-Type' : 'application/json', 'Access-token': '123456'}

r = requests.post(url,data=json.dumps(args),headers=cabecera)

print(r.url)
if r.status_code == 200:
    cabecera_response = r.headers
    server = cabecera_response['Server']
    print(cabecera_response)
    print(server)
