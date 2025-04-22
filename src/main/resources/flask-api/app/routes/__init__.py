"""
Paquete que define y registra las diferentes rutas para nuestra API.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.1.0, 20 de Abril de 2025.
"""

from .item_routes import item_bp
from .move_routes import move_bp
from .pokemon_routes import pokemon_bp

def register_routes(app):
    """
    Registra las diferentes rutas de la API que podrán a llegar a ser consumidas
    dentro de una aplicación Flask.

    Parámetros:
    ------------
    app
        Aplicación Flask donde se registran las diferentes rutas de la
        API que podrán a llegar a ser consumidas.
    """
    app.register_blueprint(item_bp, url_prefix='/api')
    app.register_blueprint(move_bp, url_prefix='/api')
    app.register_blueprint(pokemon_bp, url_prefix='/api')