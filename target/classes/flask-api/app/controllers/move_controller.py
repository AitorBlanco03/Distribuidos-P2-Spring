"""
Define e implementa la lógica para obtener y procesar todos los
movimientos Pokémon disponibles dentro del universo de Pokémon desde
la PokeAPI.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 21 de Abril de 2025.
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
                'type': type.capitalize(),
                'category': category.capitalize(),
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
            'type': '???',
            'category': '???',
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