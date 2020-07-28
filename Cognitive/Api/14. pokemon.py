import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/charizard'

response = requests.get(url)

if response.status_code == 200:
    lista = response.json()  # Obtener el resultado en formato json
    print(lista)
    # Obtener el resultado de los valores de lista
    results = lista.get('results',[])
    # print(results)
    if results:
        for pokemon in results:
            name = pokemon['name']
            urlx = pokemon['url']
            responsex = requests.get(urlx)
            if responsex.status_code == 200:
                caracteristicas = responsex.json()
                # Se desea obtener los valores del diccionario
                sprites = caracteristicas['sprites']
                print(name + ':')
                # print('   back default: ' + sprites['back_default'])
                # print('   back shiny: ' + sprites['back_shiny'])
                # print('   front defualt: ' + sprites['front_default'])
                # print('   front shiny: ' + sprites['front_shiny'])
