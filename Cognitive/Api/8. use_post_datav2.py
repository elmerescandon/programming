import requests
import json

url = 'http://httpbin.org/post'

args = {'id' : '1','pass' : '123'}

# Revisar si el proveedor lo carga en data o forms
r = requests.post(url,data=json.dumps(args))
# json.dumps escribe los vavlores en data/json en vez de forms
# usando data antes se escribíá en forms únicamente
print(r.url)

if r.status_code == 200:
    print(r.content)
