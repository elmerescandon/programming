import requests

# ====================
# Primera versión
# ====================
# URL de la página a pedir información
# url = 'http://httpbin.org/get'
#
# args = {
#     'id': '1',
#     'pass': '123'
# }

# r = requests.get(url,params=args)
#
# if r.status_code == 200:
#     response_json = r.json()
#     # print(response_json)
#     origin = response_json['origin']
#     print(origin)

# ====================
# Segunda versión
# ====================
#
# urlv2 = 'http://httpbin.org/get?id=raul&pass=raulescandon'
# rv2 = requests.get(url)
#
# if rv2.status_code == 200:
#     contentv2 = r.content
#     print(contentv2)

# ====================
# Tercera versión
# ====================

urlv3 = 'http://httpbin.org/get'
argsv3 = {
    'id':'raulescandon',
    'pass':'raulo123'
}

rv3 = requests.get(urlv3,params=argsv3)
if rv3.status_code == 200:
    response_jsonv3 = rv3.json()
    print(response_jsonv3)
    # Obtener algún argumento de la respuesta
    origin = response_jsonv3['origin']
    print(origin)
