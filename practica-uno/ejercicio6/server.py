from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Animal:
    def __init__(self, nombre, especie, genero, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso


class Mamifero(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "Mamífero"


class Ave(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "Ave"


class Reptil(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "Reptil"


class Anfibio(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "Anfibio"


class Pez(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "Pez"


class AnimalFactory:
    @staticmethod
    def create_animal(tipo, nombre, especie, genero, edad, peso):
        if tipo == "Mamífero":
            return Mamifero(nombre, especie, genero, edad, peso)
        elif tipo == "Ave":
            return Ave(nombre, especie, genero, edad, peso)
        elif tipo == "Reptil":
            return Reptil(nombre, especie, genero, edad, peso)
        elif tipo == "Anfibio":
            return Anfibio(nombre, especie, genero, edad, peso)
        elif tipo == "Pez":
            return Pez(nombre, especie, genero, edad, peso)
        else:
            raise ValueError("Tipo de animal no válido")


class AnimalRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/animal":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            tipo = request_data.get("tipo")
            nombre = request_data.get("nombre")
            especie = request_data.get("especie")
            genero = request_data.get("genero")
            edad = request_data.get("edad")
            peso = request_data.get("peso")

            animal_factory = AnimalFactory()
            animal = animal_factory.create_animal(tipo, nombre, especie, genero, edad, peso)

            response_data = {"message": f"{animal.tipo} {animal.nombre} creado"}
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, AnimalRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
