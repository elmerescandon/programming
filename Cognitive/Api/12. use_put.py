import requests
import json

url = 'http://httpbin.org/put'

# Put es para actualizar los valores
args = {'id' : '1','pass' : '123'}
cabecera = {'Content-Type' : 'application/json', 'Access-token': '123456'}

r = requests.put(url,data=json.dumps(args),headers=cabecera)

print(r.url)

if r.status_code == 200:
    cabecera_response = r.headers
    server = cabecera_response['Server']
    print(cabecera_response)
    print(server)
