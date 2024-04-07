# Importamos la biblioteca requests para hacer peticiones HTTP
import requests

# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/animal"

# Definimos los encabezados HTTP que vamos a enviar con la petición
headers = {"Content-Type": "application/json"}

# Definimos los datos del animal a crear
data1 = {
    "tipo": "Mamífero",
    "nombre": "León",
    "especie": "Panthera leo",
    "genero": "Macho",
    "edad": 5,
    "peso": 200
}

# Hacemos una petición POST a la URL con los datos y encabezados definidos
response = requests.post(url, json=data1, headers=headers)

if response.status_code == 201:
    print(response.text)
else:
    print("Error creando animal:", response.text)

# Definimos otros datos para crear un nuevo animal de tipo "Ave"
data2 = {
    "tipo": "Ave",
    "nombre": "Águila",
    "especie": "Aquila chrysaetos",
    "genero": "Hembra",
    "edad": 3,
    "peso": 5
}

# Hacemos otra petición POST a la URL con los nuevos datos y los mismos encabezados
response = requests.post(url, json=data2, headers=headers)

if response.status_code == 201:
    print(response.text)
else:
    print("Error creando animal:", response.text)
