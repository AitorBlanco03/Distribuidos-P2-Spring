"""
Inicializa y configura todas las rutas que tienen como objetivo la búsqueda y
filtrado de los movimientos disponibles dentro del universo de Pokémon.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 21 de Abril de 2025.
"""

from flask import Blueprint
from ..controllers.move_controller import get_moves

# Creamos un Blueprint para registrar todas las diferentes rutas asociadas
# a la búsqueda y filtrado de los movimientos disponibles dentro del universo Pokémon.
move_bp = Blueprint('move_bp', __name__)

# Registramos todas las rutas junto a sus operaciones HTTP correspodientes.
move_bp.route('/moves', methods=['GET'])(get_moves)