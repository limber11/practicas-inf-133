import requests

url = "http://localhost:8000/"

# POST /partidas
element = input("Elige piedra, papel o tijera: ").lower()
response = requests.request(method="POST", url=url + "partidas", json={"elemento": element})
print("Respuesta del servidor:", response.text)

# GET /partidas
response = requests.request(method="GET", url=url + "partidas")
print("Todas las partidas:", response.text)

# GET /partidas?resultado={resultado}
result = input("Ingrese el resultado (ganó, perdió o empató): ").lower()
response = requests.request(method="GET", url=url + f"partidas?resultado={result}")
print(f"Partidas con resultado '{result}':", response.text)
