from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

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

    def crear_paciente(self, ci, nombre, apellido, edad, genero, diagnostico, doctor):
        paciente = Paciente(ci, nombre, apellido, edad, genero, diagnostico, doctor)
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

            hospital.crear_paciente(**request_data)

            self.response_handler(201, {"message": "Paciente creado exitosamente"})
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})

    def do_GET(self):
        if self.path == "/pacientes":
            pacientes = [vars(paciente) for paciente in hospital.listar_pacientes()]
            self.response_handler(200, pacientes)
        elif self.path.startswith("/pacientes/"):
            ci = self.path.split("/")[-1]
            paciente = hospital.buscar_paciente_por_ci(ci)
            if paciente:
                self.response_handler(200, vars(paciente))
            else:
                self.response_handler(404, {"Error": "Paciente no encontrado"})
        elif self.path.startswith("/pacientes/?diagnostico="):
            diagnostico = parse_qs(urlparse(self.path).query)["diagnostico"][0]
            pacientes = [vars(paciente) for paciente in hospital.listar_pacientes_por_diagnostico(diagnostico)]
            self.response_handler(200, pacientes)
        elif self.path.startswith("/pacientes/?doctor="):
            doctor = parse_qs(urlparse(self.path).query)["doctor"][0]
            pacientes = [vars(paciente) for paciente in hospital.listar_pacientes_por_doctor(doctor)]
            self.response_handler(200, pacientes)
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})

    def do_PUT(self):
        if self.path.startswith("/pacientes/"):
            ci = self.path.split("/")[-1]
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            if hospital.actualizar_paciente(ci, **request_data):
                self.response_handler(200, {"message": "Paciente actualizado exitosamente"})
            else:
                self.response_handler(404, {"Error": "Paciente no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})

    def do_DELETE(self):
        if self.path.startswith("/pacientes/"):
            ci = self.path.split("/")[-1]
            if hospital.eliminar_paciente(ci):
                self.response_handler(200, {"message": "Paciente eliminado exitosamente"})
            else:
                self.response_handler(404, {"Error": "Paciente no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})

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
