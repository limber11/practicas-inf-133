import requests
import json

# Definimos la URL base del servidor
base_url = "http://localhost:8000"

# Función para hacer una solicitud POST para crear un nuevo paciente
def crear_paciente(ci, nombre, apellido, edad, genero, diagnostico, doctor):
    url = base_url + "/pacientes"
    headers = {"Content-Type": "application/json"}
    data = {
        "ci": ci,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "genero": genero,
        "diagnostico": diagnostico,
        "doctor": doctor
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Paciente creado exitosamente.")
    else:
        print("Error al crear el paciente:", response.text)

# Función para hacer una solicitud GET para obtener la lista de todos los pacientes
def listar_pacientes():
    url = base_url + "/pacientes"
    response = requests.get(url)
    if response.status_code == 200:
        pacientes = response.json()
        print("Lista de pacientes:")
        for paciente in pacientes:
            print(paciente)
    else:
        print("Error al obtener la lista de pacientes:", response.text)

# Función para hacer una solicitud GET para obtener la información de un paciente por CI
def buscar_paciente_por_ci(ci):
    url = base_url + "/pacientes/" + ci
    response = requests.get(url)
    if response.status_code == 200:
        paciente = response.json()
        print("Información del paciente con CI", ci + ":")
        print(paciente)
    else:
        print("Error al buscar el paciente:", response.text)

# Función para hacer una solicitud GET para obtener la lista de pacientes por diagnóstico
def listar_pacientes_por_diagnostico(diagnostico):
    url = base_url + "/pacientes/?diagnostico=" + diagnostico
    response = requests.get(url)
    if response.status_code == 200:
        pacientes = response.json()
        print("Lista de pacientes con diagnóstico", diagnostico + ":")
        for paciente in pacientes:
            print(paciente)
    else:
        print("Error al obtener la lista de pacientes por diagnóstico:", response.text)

# Función para hacer una solicitud GET para obtener la lista de pacientes atendidos por un doctor
def listar_pacientes_por_doctor(doctor):
    url = base_url + "/pacientes/?doctor=" + doctor
    response = requests.get(url)
    if response.status_code == 200:
        pacientes = response.json()
        print("Lista de pacientes atendidos por el doctor", doctor + ":")
        for paciente in pacientes:
            print(paciente)
    else:
        print("Error al obtener la lista de pacientes por doctor:", response.text)

# Función para hacer una solicitud PUT para actualizar la información de un paciente por CI
def actualizar_paciente(ci, nombre, apellido, edad, genero, diagnostico, doctor):
    url = base_url + "/pacientes/" + ci
    headers = {"Content-Type": "application/json"}
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "genero": genero,
        "diagnostico": diagnostico,
        "doctor": doctor
    }
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Información del paciente actualizada exitosamente.")
    else:
        print("Error al actualizar la información del paciente:", response.text)

# Función para hacer una solicitud DELETE para eliminar un paciente por CI
def eliminar_paciente(ci):
    url = base_url + "/pacientes/" + ci
    response = requests.delete(url)
    if response.status_code == 200:
        print("Paciente eliminado exitosamente.")
    else:
        print("Error al eliminar el paciente:", response.text)

# Ejemplos de uso de las funciones
#crear_paciente("1234567", "Juan", "Perez", 30, "Masculino", "Gripe", "Dr. Rodriguez")
#listar_pacientes()
#buscar_paciente_por_ci("1234567")
#listar_pacientes_por_diagnostico("Gripe")
#listar_pacientes_por_doctor("Dr. Rodriguez")
#actualizar_paciente("1234567", "Juan", "Perez", 35, "Masculino", "Gripe", "Dr. Rodriguez")
#eliminar_paciente("1234567")
