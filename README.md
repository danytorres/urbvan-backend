# API Employees

Api empaquetado en docker file y compuesto con docker-compose, creando un contenedor empaquetando el proyecto django y conectandose con otro contenedor con postgresql

Al momento de crear los contenedores se carga de inmediato un comando especial para detectar si tiene un usario administrador y si no lo crea y activa el servidor con gunicorn con 5 workers

## Funcionamiento

El api de busqueda funciona con el siguiente link:

```
GET /users/ # Retorna todos los usarios

POST /users/ # Crea un nuevo usario

GET /users/{id identificador de employee} # Retorna el usuario con identificador id

PUT /users/{id identificador de employee} # Modifica el usuario con identificador id

DELETE /users/{id identificador de employee} # Elimina a el usuario con identificador id
```

## Variables de entorno

las variables de entorno dentro de docker compose son las siguientespara crear el super usuario

      - DJANGO_SUPERUSER_USERNAME=
      - DJANGO_SUPERUSER_PASSWORD=
      - DJANGO_SUPERUSER_EMAIL=

Al momento de empezar se verifica si ya se tiene este super usuario y si no se crea.

