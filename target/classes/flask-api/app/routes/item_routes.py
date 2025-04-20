"""
Inicializa y configura todos las rutas que tienen como objetivo la búsqueda y
filtrado de los objetos dentro del universo de Pokémon.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 20 de Abril de 2025.
"""

from flask import Blueprint
from ..controllers.item_controller import get_items

# Creamos un Blueprint para registrar todas las diferentes rutas asociadas
# a la búsqueda y filtrado de los objetos dentro del universo de Pokémon.
item_bp = Blueprint('item_bp', __name__)

# Registramos todas las rutas junto a sus operaciones HTTP correspondientes.
item_bp.route('/items', methods=['GET'])(get_items)