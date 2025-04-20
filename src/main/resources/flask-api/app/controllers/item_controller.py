"""
Define e implementa la lógica para obtener y procesar todos los
objetos dentro del universo Pokémon desde la PokeAPI.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 20 de Abril de 2025.
"""

from flask import Response, jsonify
import json
import requests

def get_items():
    """
    Busca, obtiene y procesa toda la información de los objetos dentro
    del universo Pokémon utilizando como base la PokeAPI.

    Returns:
    ---------
    JSON con la información de los objetos después de realizar la petición a la
    PokeAPI.
    """
    # Definimos la URL base de la PokeAPI para obtener la información de los objetos.
    url = "https://pokeapi.co/api/v2/item/"

    try:
        # Realizamos una petición a la PokeAPI para procesar y obtener la información de los objetos.
        response = requests.get(url)
        # Procesamos la respuesta para buscar y filtrar la información relevante de los objetos.
        data = response.json()
        items = []

        # Iteramos sobre cada uno de los objetos obtenidos y, buscamos y filtramos su información.
        for item in data['results']:
            # Realizamos una petición sobre la url propia del objeto para procesar y extraer su información.
            item_detail_response = requests.get(item['url'])
            item_detail = item_detail_response.json()

            # Obtenemos el nombre y la categoría a los que pertenece el objeto actual.
            name = item_detail.get('name', '')
            category = item_detail.get('category', {}).get('name', '')
            effect = ''

            # Buscamos la descripción del objeto en español entre todas las descripciones válidas para ese objeto.
            for entry in item_detail.get('flavor_text_entries', []):
                if entry.get('language', {}).get('name') == 'es':
                    effect = entry.get('text', '')
                    break

            # Antes de registrar los datos del objeto, procesamos el nombre y categoria para que tengan un formato correcto.
            name = ' '.join([item_name.capitalize() for item_name in name.split('-')])
            category = ' '.join([item_category.capitalize() for item_category in category.split('-')])

            # Registramos la información obtenida de ese objeto a través de la PokeApi.
            items.append({
                'name': name,
                'category': category,
                'effect': effect
            })

        # Procesamos la información obtenida en forma de JSON codificando su contenido en UTF-8.
        response_data = json.dumps(items, ensure_ascii=False)
        return Response(response_data, content_type='application/json; charset=utf-8')

    except Exception as e:
        # Si ocurre algún error durante el proceso, reinterpretaremos el error como un código 500.
        return jsonify({"error": "Error al obtener la información de los objetos."}), 500