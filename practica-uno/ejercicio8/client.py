import requests
import json

# Definimos la URL base del servidor donde se encuentra la API
base_url = "http://localhost:8000"

# Función para realizar una solicitud POST para crear un mensaje encriptado
def create_message(content):
    endpoint = "/mensajes"
    url = base_url + endpoint
    headers = {"Content-Type": "application/json"}
    data = {"contenido": content}
    response = requests.post(url, json=data, headers=headers)
    return response

# Función para realizar una solicitud GET para obtener todos los mensajes encriptados
def get_all_messages():
    endpoint = "/mensajes"
    url = base_url + endpoint
    response = requests.get(url)
    return response

# Función para realizar una solicitud GET para obtener un mensaje encriptado por ID
def get_message_by_id(message_id):
    endpoint = f"/mensajes/{message_id}"
    url = base_url + endpoint
    response = requests.get(url)
    return response

# Función para realizar una solicitud PUT para actualizar el contenido de un mensaje encriptado por ID
def update_message_content(message_id, new_content):
    endpoint = f"/mensajes/{message_id}"
    url = base_url + endpoint
    headers = {"Content-Type": "application/json"}
    data = {"contenido": new_content}
    response = requests.put(url, json=data, headers=headers)
    return response

# Función para realizar una solicitud DELETE para eliminar un mensaje encriptado por ID
def delete_message(message_id):
    endpoint = f"/mensajes/{message_id}"
    url = base_url + endpoint
    response = requests.delete(url)
    return response

# Ejemplo de uso de las funciones definidas

# Crear un mensaje encriptado
content = "Este es un mensaje secreto"
response = create_message(content)
if response.status_code == 201:
    print("Mensaje creado exitosamente")
    print("ID del mensaje:", response.json()["id"])
else:
    print("Error al crear el mensaje:", response.text)

# Obtener todos los mensajes encriptados
response = get_all_messages()
if response.status_code == 200:
    messages = response.json()
    print("Todos los mensajes encriptados:")
    for message in messages:
        print("ID:", message["id"])
        print("Contenido:", message["contenido"])
        print("Contenido encriptado:", message["contenido_encriptado"])
        print()
else:
    print("Error al obtener todos los mensajes:", response.text)

# Obtener un mensaje encriptado por ID
message_id = 1  # Reemplaza con el ID del mensaje que deseas obtener
response = get_message_by_id(message_id)
if response.status_code == 200:
    message = response.json()
    print("Mensaje encriptado encontrado:")
    print("ID:", message["id"])
    print("Contenido:", message["contenido"])
    print("Contenido encriptado:", message["contenido_encriptado"])
else:
    print("Error al obtener el mensaje encriptado por ID:", response.text)

# Actualizar el contenido de un mensaje encriptado por ID
message_id = 1  # Reemplaza con el ID del mensaje que deseas actualizar
new_content = "Este es el nuevo contenido del mensaje"
response = update_message_content(message_id, new_content)
if response.status_code == 200:
    print("Contenido del mensaje actualizado exitosamente")
else:
    print("Error al actualizar el contenido del mensaje:", response.text)

# Eliminar un mensaje encriptado por ID
message_id = 1  # Reemplaza con el ID del mensaje que deseas eliminar
response = delete_message(message_id)
if response.status_code == 200:
    print("Mensaje eliminado exitosamente")
else:
    print("Error al eliminar el mensaje:", response.text)
