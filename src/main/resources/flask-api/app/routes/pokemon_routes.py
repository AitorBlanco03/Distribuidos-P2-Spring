"""
Inicializa y configura todas las rutas que tienen como objetivo la búsqueda
y filtrado de todos los Pokemóns dentro del universo de Pokémon.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 22 de Abril de 2025.
"""

from flask import Blueprint, request
from ..controllers.pokemon_controller import get_pokemons

# Creamos un Blueprint para registrar todas las diferentes rutas asociadas
# a la búsqueda y filtrado de todos los Pokemóns dentro del universo de Pokémon.
pokemon_bp = Blueprint('pokemon_bp', __name__)

# Registramos todas las rutas junto a sus operaciones HTTP correspondientes.
@pokemon_bp.route('/pokemons', methods=['GET'])
def pokemon_route():
    """
    Define e implementa la lógica de la ruta de API para la búsqueda y filtrado
    de todos los Pokémons dentro del universo Pokémon.
    """
    try:
        # Obtenemos de la URL, la página cuya información queremos conocer.
        page = int(request.args.get('page', 0))
        return get_pokemons(page)
    except ValueError:
        # Si obtenemos un error al obtener la página, reinterpretaremos el error como un 200.
        return {
            'previous': '',
            'next': '',
            'pokemons': [{
                'id': 0,
                'name': '???',
                'sprite': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png',
                'types': ['???']
            }]
        }, 200