import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple para listar todas las plantas
query_lista_plantas = """
{
    plantas {
        id
        nombreComun
        especie
        edadMeses
        alturaCm
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para listar todas las plantas
response = requests.post(url, json={'query': query_lista_plantas})
print("Lista de todas las plantas:")
print(response.text)

# Definir la consulta GraphQL con parámetros para buscar plantas por especie
query_buscar_por_especie = """
{
    plantaPorEspecie(especie: "Rosa") {
        id
        nombreComun
        especie
        edadMeses
        alturaCm
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para buscar plantas por especie
response = requests.post(url, json={'query': query_buscar_por_especie})
print("\nPlantas de la especie 'Rosa':")
print(response.text)

# Definir la consulta GraphQL para crear una nueva planta
query_crear_planta = """
mutation {
    crearPlanta(nombreComun: "Orquídea", especie: "Orchidaceae", edadMeses: 6, alturaCm: 25, frutos: false) {
        planta {
            id
            nombreComun
            especie
            edadMeses
            alturaCm
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para crear una nueva planta
response = requests.post(url, json={'query': query_crear_planta})
print("\nRespuesta al crear una nueva planta:")
print(response.text)

# Lista de todas las plantas después de la creación
response = requests.post(url, json={'query': query_lista_plantas})
print("\nLista de todas las plantas después de la creación:")
print(response.text)

# Definir la consulta GraphQL para eliminar una planta
query_eliminar_planta = """
mutation {
    eliminarPlanta(id: 2) {
        planta {
            id
            nombreComun
            especie
            edadMeses
            alturaCm
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para eliminar una planta
response = requests.post(url, json={'query': query_eliminar_planta})
print("\nRespuesta al eliminar una planta:")
print(response.text)

# Lista de todas las plantas después de la eliminación
response = requests.post(url, json={'query': query_lista_plantas})
print("\nLista de todas las plantas después de la eliminación:")
print(response.text)
