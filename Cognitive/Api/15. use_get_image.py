import requests

url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/149.png'
# realiza la petición de descargar y
# stream=True deja la conexion abierta
response = requests.get(url, stream=True)
# wb = abrir archivo en formato escritura
with open('image.png','wb') as file:
    for data in response.iter_content():
        file.write(data)
response.close()  # cerramos la conexion
