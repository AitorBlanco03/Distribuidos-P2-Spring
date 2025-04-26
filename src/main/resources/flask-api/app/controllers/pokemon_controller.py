"""
Define e implementa la lógica para obtener y procesar la información de
todos los Pokémons en el universo Pokémon, organizados en forma de páginas.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.2.0, 23 de Abril de 2024.
"""

from flask import Response, jsonify
import json
import requests

def get_pokemons(page):
    """
    Busca, procesa y obtiene toda la información de todos los Pokémons en
    forma de página.
    """
    # Calculamos la página máxima que permitiremos obtener.
    size = 20
    total_pokemons = 1025
    max_page = (total_pokemons + size - 1) // size

    # Calculamos el offset para obtener los Pokémon disponibles en la página.
    offset = (page - 1) * size

    # Si el offset supera los 1025 Pokémon permitidos, no mostraremos más información.
    if page > max_page:
        page_info = {
            'previous': None,
            'next': None,
            'pokemons': []
        }
        response_data = json.dumps(page_info, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')

    # Obtenemos la URL de la PokeAPI para obtener la página solicitada con su información.
    url = f"https://pokeapi.co/api/v2/pokemon?limit={size}&offset={offset}"

    try:
        # Realizamos una petición a la PokeAPI y procesamos su respuesta.
        response = requests.get(url)
        data = response.json()

        # Obtenemos los detalles de la página solicitada sobre la respuesta obtenida.
        page_info = {
            'previous': data['previous'],
            'next': data['next'],
            'pokemons': []
        }

        # Para cada Pokemon de la página obtenemos su información.
        for pokemon in data['results']:
            pokemon_data = requests.get(pokemon['url']).json()
            pokemon_info = {
                'id': pokemon_data['id'],
                'name': pokemon_data['name'],
                'sprite': pokemon_data['sprites']['front_default'],
                'types': [format_move_type(t['type']['name']) for t in pokemon_data['types']]
            }
            page_info['pokemons'].append(pokemon_info)

        # Procesamos la información obtenida y la devolvemos en forma de JSON codificando su contenido en UTF-8.
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
                'types': ['']
            }]
        }
        response_data = json.dumps(page_info, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')


def format_move_type(move_type):
    """
    Procesa el tipo del movimiento recibido desde la PokeAPI y obtiene la URL asociada
    a su representación dentro de la tabla.

    Parámetros:
    ------------
    move_type: str
        Tipo del movimiento recibido desde la PokeAPI.

    Returns:
    ---------
    URL de la representación del tipo del movimiento dentro de la tabla.
    """
    # Definimos la URL asociada a cada uno de los tipos.
    move_types = {
        "steel": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/9/98/latest/20230108233610/Tipo_acero_EpEc.png/80px-Tipo_acero_EpEc.png",
        "water": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/9/90/latest/20230109223300/Tipo_agua_EpEc.png/80px-Tipo_agua_EpEc.png",
        "bug": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/a/a1/latest/20230109223320/Tipo_bicho_EpEc.png/80px-Tipo_bicho_EpEc.png",
        "dragon": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/e/e3/latest/20230109223334/Tipo_drag%C3%B3n_EpEc.png/80px-Tipo_drag%C3%B3n_EpEc.png",
        "electric": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/3/3c/latest/20230109223352/Tipo_el%C3%A9ctrico_EpEc.png/80px-Tipo_el%C3%A9ctrico_EpEc.png",
        "ghost": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/3/36/latest/20230109223409/Tipo_fantasma_EpEc.png/80px-Tipo_fantasma_EpEc.png",
        "fire": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/e/ed/latest/20230109223425/Tipo_fuego_EpEc.png/80px-Tipo_fuego_EpEc.png",
        "fairy": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/9/94/latest/20230109223445/Tipo_hada_EpEc.png/80px-Tipo_hada_EpEc.png",
        "ice": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/f/fd/latest/20230109223459/Tipo_hielo_EpEc.png/80px-Tipo_hielo_EpEc.png",
        "fighting": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/5/52/latest/20230109223516/Tipo_lucha_EpEc.png/80px-Tipo_lucha_EpEc.png",
        "normal": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/a/a7/latest/20230109215235/Tipo_normal_EpEc.png/80px-Tipo_normal_EpEc.png",
        "grass": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/1/1d/latest/20230109223536/Tipo_planta_EpEc.png/80px-Tipo_planta_EpEc.png",
        "psychic": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/d/d7/latest/20230109223552/Tipo_ps%C3%ADquico_EpEc.png/80px-Tipo_ps%C3%ADquico_EpEc.png",
        "rock": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/3/31/latest/20230109223608/Tipo_roca_EpEc.png/80px-Tipo_roca_EpEc.png",
        "dark": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/0/01/latest/20230109223623/Tipo_siniestro_EpEc.png/80px-Tipo_siniestro_EpEc.png",
        "ground": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/6/68/latest/20230109223637/Tipo_tierra_EpEc.png/80px-Tipo_tierra_EpEc.png",
        "poison": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/3/3a/latest/20230109223652/Tipo_veneno_EpEc.png/80px-Tipo_veneno_EpEc.png",
        "flying": "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/9/92/latest/20230109223707/Tipo_volador_EpEc.png/80px-Tipo_volador_EpEc.png"
    }

    # Devolvemos la representación de ese tipo dentro de la tabla.
    return move_types.get(move_type, '')