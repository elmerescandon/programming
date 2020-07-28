import requests
import json
# PC3 - Cognitiv
# Raúl Escandón Tufino

url = 'https://pokeapi.co/api/v2/pokemon/dragonite'
# Se escogió el pokemon Dragonite
print("Pregunta 1: Cognitive - Dragonite")
# Guardar en responde el contenido de lo leído por el URL
response = requests.get(url)

if response.status_code == 200:
    lista = response.json()  # Obtener el resultado en formato json

    # Obtener el resultado de los valores de lista
    habilidades = lista.get('abilities',[])

    print("Nombre de las habilidades")
    # Recorrer todo el diccionario
    for hab in range(len(habilidades)):
        # Obtener el objeto individual de habilidades
        tmp = habilidades[hab]

        # Escoger a caracteristicas ability
        ability = tmp.get('ability')

        # Recuperar el nombre de la habilidad
        nombre_habilidad = ability.get('name')
        print(nombre_habilidad)
