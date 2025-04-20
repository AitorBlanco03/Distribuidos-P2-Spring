"""
Paquete encargado de inicializar y configurar la aplicación Flask, y de
definir y registrar las diferentes rutas de la API a ser consumidas.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 20 de Abril de 2025.
"""

from flask import Flask
from .routes import register_routes

def create_app():
    """
    Crea, inicializa y configura la aplicación Flask, y registra las
    diferentes rutas de la API que podrán a llegar a ser consumidas.

    Returns:
    ---------
        Aplicación Flask con las diferentes rutas de la AI que podrán a
        llegar a ser consumidas.
    """
    # Creamos, inicializamos y configuramos la aplicación Flask.
    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Registramos las diferentes rutas de la API que podrán a llegar a ser consumidas.
    register_routes(app)

    # Devolvemos la aplicación Flask creada y configurada con las rutas de la API.
    return app