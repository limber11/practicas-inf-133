from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

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
        return Paciente(self.ci, self.nombre, self.apellido, self.edad, self.genero, self.diagnostico, self.doctor)

class Paciente:
    def __init__(self, ci, nombre, apellido, edad, genero, diagnostico, doctor):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.diagnostico = diagnostico
        self.doctor = doctor

class Hospital:
    def __init__(self):
        self.pacientes = []

    def crear_paciente(self, paciente):
        self.pacientes.append(paciente)

    def listar_pacientes(self):
        return self.pacientes

    def buscar_paciente_por_ci(self, ci):
        for paciente in self.pacientes:
            if paciente.ci == ci:
                return paciente
        return None

    def listar_pacientes_por_diagnostico(self, diagnostico):
        return [paciente for paciente in self.pacientes if paciente.diagnostico == diagnostico]

    def listar_pacientes_por_doctor(self, doctor):
        return [paciente for paciente in self.pacientes if paciente.doctor == doctor]

    def actualizar_paciente(self, ci, nombre, apellido, edad, genero, diagnostico, doctor):
        for paciente in self.pacientes:
            if paciente.ci == ci:
                paciente.nombre = nombre
                paciente.apellido = apellido
                paciente.edad = edad
                paciente.genero = genero
                paciente.diagnostico = diagnostico
                paciente.doctor = doctor
                return True
        return False

    def eliminar_paciente(self, ci):
        for i, paciente in enumerate(self.pacientes):
            if paciente.ci == ci:
                self.pacientes.pop(i)
                return True
        return False

hospital = Hospital()

class PatientRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/pacientes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            paciente_builder = PacienteBuilder()
            paciente = paciente_builder.set_ci(request_data['ci']) \
                                        .set_nombre(request_data['nombre']) \
                                        .set_apellido(request_data['apellido']) \
                                        .set_edad(request_data['edad']) \
                                        .set_genero(request_data['genero']) \
                                        .set_diagnostico(request_data['diagnostico']) \
                                        .set_doctor(request_data['doctor']) \
                                        .build()

            hospital.crear_paciente(paciente)

            self.response_handler(201, {"message": "Paciente creado exitosamente"})
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})

    # Resto del código sin cambios...

def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, PatientRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()
