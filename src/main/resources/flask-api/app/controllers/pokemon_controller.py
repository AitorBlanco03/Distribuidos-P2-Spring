"""
Define e implementa la lógica para obtener y procesar la información de
todos los Pokémons en el universo Pokémon, organizados en forma de páginas.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 22 de Abril de 2024.
"""

from flask import Response, jsonify
import json
import requests

def get_pokemons(page):
    """
    Busca, obtiene y procesa la información de Pokémons en forma de
    páginas.

    Parámetros:
    ------------
    page: int
        Número de la página que se desea obtener.

    Returns:
    ---------
    JSON con la información de los Pokémons asociados a la página que
    se desea obtener.
    """
    # Calculamos el offset junto a la url de la API para obtener los Pokémon de la página actual.
    size = 20
    offset = page * size
    url = f"https://pokeapi.co/api/v2/pokemon?limit={size}&offset={offset}"

    try:
        # Realizamos una petición a la PokeAPI para obtener la información de la página actual.
        response = requests.get(url)
        # Procesamos la respuesta para obtener la información de la página actual.
        data = response.json()

        # Obtenemos los detalles de la página actual sobre la respuesta obtenida.
        page_info = {
            'previous': data['previous'],
            'next': data['next'],
            'pokemons': []
        }

        # Para Pokémon asociado a la página obtenemos su información y la guardamos.
        for pokemon in data['results']:
            pokemon_data = requests.get(pokemon['url']).json()
            pokemon_info = {
                'id': pokemon_data['id'],
                'name': pokemon_data['name'],
                'sprite': pokemon_data['sprites']['front_default'],
                'types': [t['type']['name'] for t in pokemon_data['types']]
            }
            page_info['pokemons'].append(pokemon_info)

        # Procesamos la información obtenida en forma de JSON codificando su contenido en UTF-8.
        response_data = json.dumps(page_info, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')

    except Exception as e:
        # Si ocurre algún error, se reinterpreta con un 200 pero se inventará unos datos fícticos para la página.
        page_info = {
            'previous': '',
            'next': '',
            'pokemons': [{
                'id': 0,
                'name': '???',
                'sprite': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png',
                'types': ['???']
            }]
        }
        response_data = json.dumps(page_info, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')