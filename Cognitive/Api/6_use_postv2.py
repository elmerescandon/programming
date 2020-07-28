import requests
import json

url = 'http://httpbin.org/post'

args = {
    'id' : '1',
    'pass' : '123'
}

# Ahora se añade Json en vez de args
r = requests.post(url,json=args)
# Json guarda los valores en data en vez de forms

print(r.url)

if r.status_code == 200:
    print(r.content)
