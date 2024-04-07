import requests
import json

# Definimos la URL base del servidor
base_url = "http://localhost:8000"

class PacienteBuilder:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.genero = None
        self.diagnostico = None
        self.doctor = None

    def set_ci(self, ci):
        self.ci = ci
        return self

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_apellido(self, apellido):
        self.apellido = apellido
        return self

    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_genero(self, genero):
        self.genero = genero
        return self

    def set_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico
        return self

    def set_doctor(self, doctor):
        self.doctor = doctor
        return self

    def build(self):
        return {
            "ci": self.ci,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "genero": self.genero,
            "diagnostico": self.diagnostico,
            "doctor": self.doctor
        }

# Función para hacer una solicitud POST para crear un nuevo paciente
def crear_paciente(ci, nombre, apellido, edad, genero, diagnostico, doctor):
    url = base_url + "/pacientes"
    headers = {"Content-Type": "application/json"}
    paciente_builder = PacienteBuilder()
    paciente_data = paciente_builder.set_ci(ci) \
                                    .set_nombre(nombre) \
                                    .set_apellido(apellido) \
                                    .set_edad(edad) \
                                    .set_genero(genero) \
                                    .set_diagnostico(diagnostico) \
                                    .set_doctor(doctor) \
                                    .build()
    response = requests.post(url, json=paciente_data, headers=headers)
    if response.status_code == 201:
        print("Paciente creado exitosamente.")
    else:
        print("Error al crear el paciente:", response.text)
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
# Resto del código sin cambios...
