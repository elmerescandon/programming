import requests
import json

url = 'http://httpbin.org/get'

args = {'id': 'raulo', 'pass': 'raulo'}

r = requests.get(url,params=args)

if r.status_code == 200:
    response_json = json.loads(r.text)
    print(response_json)
    origin = response_json['origin']
    print(origin)
