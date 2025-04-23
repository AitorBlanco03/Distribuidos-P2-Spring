"""
Define e implementa la lógica para obtener y procesar todos los
movimientos Pokémon disponibles dentro del universo de Pokémon desde
la PokeAPI.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.1.0, 21 de Abril de 2025.
"""

from flask import Response, jsonify
import json
import requests

def get_moves():
    """
    Busca, obtiene y procesa toda la información de los movimientos
    disponibles dentro del universo Pokémon utilizando como base la PokeAPI.

    Returns:
    ---------
    JSON con la información de los movimientos disponibles de realizar la
    petición a la PokeAPI.
    """
    # Definimos la URL base de la PokeAPI para obtener la información de los movimientos.
    url = "https://pokeapi.co/api/v2/move/"

    try:
        # Realizamos una petición a la PokeAPI para procesar y obtener la información de los movimientos.
        response = requests.get(url)
        # Procesamos la respuesta para buscar y filtrar la información relevante de los movimientos.
        data = response.json()
        moves = []

        # Iteramos sobre cada uno de los onjetos obtenidos y, buscamos y filtramos su información.
        for move in data['results']:
            # Realizamos una petición para obtener los detalles concretos del movimiento actual.
            move_detail_response = requests.get(move['url'])
            move_detail = move_detail_response.json()

            # Obtenemos la información propia que caracteríza ese movimiento.
            name = ''
            type = move_detail.get('type', {}).get('name', '')
            category = move_detail.get('damage_class', {}).get('name', '')
            power = move_detail.get('power', None)
            accuracy =  move_detail.get('accuracy', None)
            pp = move_detail.get('pp', None)
            effect = ''

            # Buscamos el nombre del movimiento en español entre todos los nombres disponibles.
            for name_entry in move_detail.get('names', []):
                if name_entry.get('language', {}).get('name') == 'es':
                    name = name_entry.get('name', '')
                    break
            # Si el nombre del movimiento no se encuentra en español, usaremos el nombre que viene en ingles for defecto.
            if not name:
                name = move_detail.get('name', '')

            # Buscamos el efecto/descripción del movimiento en español entre todas las descripciones disponibles.
            for effect_entry in move_detail.get('flavor_text_entries', []):
                if effect_entry.get('language', {}).get('name') == 'es':
                    effect = effect_entry.get('flavor_text', '')
                    break
            # Si la descripción del movimiento no se encuentra en español, usaremos la descripción que viene en ingles.
            if not effect:
                for effect_entry in move_detail.get('flavor_text_entries', []):
                    if effect_entry.get('language', {}).get('name') == 'en':
                        effect = effect_entry.get('flavor_text', '')
                        break

            # Registramos la información obtenida de los movimientos desde la PokeAPI.
            moves.append({
                'name': name,
                'type': format_move_type(type),
                'category': format_move_category(category),
                'power': format_move_power(power),
                'accuracy': format_move_accuracy(accuracy),
                'pp': format_move_pp(pp),
                'effect': effect
            })

        # Procesamos la información obtenida en forma de JSON codificando su contenido en UTF-8.
        response_data = json.dumps(moves, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')

    except Exception as e:
        # Si ocurre algún error durante el proceso, reinterpretaremos el error como un código 200 pero se
        # mostrará un movimiento de tipo desconocido.
        return jsonify({
            'name': '???',
            'type': '',
            'category': '',
            'power': '???',
            'accuracy': '???',
            'pp': '???',
            'effect': '???'}), 200


def format_move_power(move_power):
    """
    Procesa y da formato a la potencia del movimiento recibido desde la PokeAPI para su correcta
    visualización dentro de la página y tabla.

    Parámetros:
    ------------
    move_power: int
        Potencia del movimiento recibida desde la PokeAPI.

    Returns:
    ---------
    Potencia del movimiento procesada y formateada para su visualización dentro de la página y tabla.
    """
    return str(move_power) if move_power is not None else "---"

def format_move_accuracy(move_accuracy):
    """
    Procesa y da formato a la precisión del movimiento recibido desde la PokeAPI para su correcta
    visualización dentro de la página y tabla.

    Parámetros:
    ------------
    move_accuracy: int
        Precisión del movimiento recibido desde la PokeAPI.

    Returns:
    ---------
    Precisión del movimiento procesada y formateada para su visualización dentro de la página y tabla.
    """
    return str(move_accuracy) if move_accuracy is not None else "---"

def format_move_pp(move_pp):
    """
    Procesa y da formato a los PP del movimiento recibido desde la PokeAPI para su correcta visualización
    dentro de la página y tabla.

    Parámetros:
    ------------
    move_pp: int
        PP del movimiento recibido desde la PokeAPI.

    Returns:
    ---------
    PP del movimiento procesado y formateado para su visualización dentro de la página y tabla.
    """
    return str(move_pp) if move_pp is not None else "---"

def format_move_category(move_category):
    """
    Procesa la categoria del movimiento recibida desde la PokeAPI y obtiene la URL asociada
    a su representación dentro de la tabla.

    Parámetros:
    ------------
    move_category: str
        Categoria del movimiento recibido desde la PokeAPI.

    Returns:
    ---------
    URL de la representación de la categoria del movimiento dentro de la tabla.
    """
    # Definimos la URL asociada a cada una de las categorías.
    move_categories = {
        "physical": "https://images.wikidexcdn.net/mwuploads/wikidex/5/54/latest/20230130142459/Clase_f%C3%ADsico_LGPE.png",
        "special": "https://images.wikidexcdn.net/mwuploads/wikidex/7/7e/latest/20230130141349/Clase_especial_LGPE.png",
        "status": "https://images.wikidexcdn.net/mwuploads/wikidex/6/63/latest/20230130142318/Clase_estado_LGPE.png"
    }

    # Devolvemos la representación de esa categoría dentro de la tabla.
    return move_categories.get(move_category, '')

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