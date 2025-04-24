"""
Punto de partida para la ejecución de la API.
Ejecuta un servidor con la aplicación Flask y la API desarrollada.

    - Autor: Aitor Blanco Fernández, abf1005@alu.ubu.es
    - Versión: 1.0.0, 20 de Abril de 2025.
"""

from app import create_app

# Creamos y configuramos la aplicación Flask que sirve como de base para nuestra API.
app = create_app()

# Iniciamos el servidor junto a la aplicación Flask.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)