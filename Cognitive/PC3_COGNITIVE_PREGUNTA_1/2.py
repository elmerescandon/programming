import requests
import json
# PC3 - Cognitiv
# Raúl Escandón Tufino

url = 'https://pokeapi.co/api/v2/pokemon/dragonite'
# Se escogió el pokemon Dragonite
print("Pregunta 1: Cognitive - Dragonite")
# Guardar en responde el contenido de lo leído por el URL
response = requests.get(url)
lista_urls = []
lista_names = []

if response.status_code == 200:
    lista = response.json()  # Obtener el resultado en formato json

    # Obtener el resultado de los valores de lista
    sprites = lista.get('sprites',[])
    print(len(sprites))
    if sprites:
        for n in sprites:
            img_url = sprites[n]
            if img_url is None:
                pass
            else:
                lista_names.append(n)
                lista_urls.append(img_url)
response.close()


for m in range(len(lista_urls)):
    url = lista_urls[m]
    name = lista_names[m]
    response = requests.get(url, stream=True)
    # wb = abrir archivo en formato escritura
    image_name = name + '.png'
    with open(image_name,'wb') as file:
        for data in response.iter_content():
            file.write(data)
    response.close()  # cerramos la conexion
