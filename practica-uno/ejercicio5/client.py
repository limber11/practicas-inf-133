import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los animales por la ruta /animales
ruta_get = url + "animales"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# POST agrega un nuevo animal por la ruta /animales
ruta_post = url + "animales"
nuevo_animal = {
    "nombre": "León",
    "especie": "Panthera leo",
    "genero": "Macho",
    "edad": 5,
    "peso": 200
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

# DELETE elimina todos los animales por la ruta /animales
ruta_eliminar = url + "animales"
eliminar_response = requests.request(method="DELETE", url=ruta_eliminar)
print(eliminar_response.text)

# POST agrega un nuevo animal por la ruta /animales
ruta_post = url + "animales"
nuevo_animal = {
    "nombre": "Tigre",
    "especie": "Panthera tigris",
    "genero": "Hembra",
    "edad": 4,
    "peso": 150
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

nuevo_animal = {
    "nombre": "Elefante",
    "especie": "Loxodonta africana",
    "genero": "Macho",
    "edad": 10,
    "peso": 4000
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

# GET busca a un animal por id /animales/{id}
ruta_filtrar_id = url + "animales/1"
filtrar_id_response = requests.request(method="GET", url=ruta_filtrar_id)
print(filtrar_id_response.text)

# PUT actualiza un animal por la ruta /animales/{id}
ruta_actualizar = url + "animales/1"
animal_actualizado = {
    "nombre": "León",
    "especie": "Panthera leo",
    "genero": "Macho",
    "edad": 6,
    "peso": 220
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=animal_actualizado
)
print(put_response.text)
