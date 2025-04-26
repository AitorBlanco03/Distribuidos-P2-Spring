# Pokémon Wiki - MVC Web App + API Flask.

Aplicación web sencilla desarrollada con el propósito de aprender y aplicar la arquitectura **Modelo-Vista-Controlador (MVC)**. Este proyecto integra una API interna construida con Flask, que actuará como un intermediario entre la aplicación web y la PokeAPI.

## ¿Cómo ejecutar el proyecto?

### 1. Clonar el repositorio.
Primero, clona el repositorio del proyecto en tu máquina local:

```
git clone https://github.com/AitorBlanco03/Distribuidos-P2-Spring.git
cd Distribuidos-P2-Spring
```

### 2. Ejecutar con Docker.
A continuación, se usará Docker para levantar los servicios necesarios:

```
docker-compose up
```

Este comando creará y levantará automáticamente los contenedores, ejecutando:

 * API Flask en ``http://localhost:5000``
 * Aplicación Web (Spring Boot): ``http://localhost:8080``

### Bibliografía.

 * [Tailwind CSS - Docs](https://tailwindcss.com/docs/styling-with-utility-classes)
 * [Geeks for Geeks - Getting Started with APIs](https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/)
 * [Geeks for Geeks - How to Call or Consume External API in Spring Boot?](https://www.geeksforgeeks.org/how-to-call-or-consume-external-api-in-spring-boot/)
 * [Cómo leer y procesar un archivo JSON en Spring Boot usando JsonNode](https://itinajero.dev/como-leer-y-procesar-un-archivo-json-en-spring-boot-usando-jsonnode/)
 * [Aplicaciones modulares con Blueprints - Flask Docs](https://flask-es.readthedocs.io/blueprints/)
