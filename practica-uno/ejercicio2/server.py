from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, Boolean, List, Schema, Field, Mutation

class Planta(ObjectType):
    id = Int()
    nombre_comun = String()
    especie = String()
    edad_meses = Int()
    altura_cm = Int()
    frutos = Boolean()

class Query(ObjectType):
    plantas = List(Planta)
    planta_por_especie = List(Planta, especie=String())
    plantas_con_frutos = List(Planta)

    def resolve_plantas(root, info):
        return plantas
    
    def resolve_planta_por_especie(root, info, especie):
        return [planta for planta in plantas if planta.especie == especie]
    
    def resolve_plantas_con_frutos(root, info):
        return [planta for planta in plantas if planta.frutos]

class CrearPlanta(Mutation):
    class Arguments:
        nombre_comun = String()
        especie = String()
        edad_meses = Int()
        altura_cm = Int()
        frutos = Boolean()

    planta = Field(Planta)

    def mutate(root, info, nombre_comun, especie, edad_meses, altura_cm, frutos):
        nueva_planta = Planta(
            id=len(plantas) + 1, 
            nombre_comun=nombre_comun,
            especie=especie,
            edad_meses=edad_meses,
            altura_cm=altura_cm,
            frutos=frutos
        )
        plantas.append(nueva_planta)
        return CrearPlanta(planta=nueva_planta)

class ActualizarPlanta(Mutation):
    class Arguments:
        id = Int()
        nombre_comun = String()
        especie = String()
        edad_meses = Int()
        altura_cm = Int()
        frutos = Boolean()

    planta = Field(Planta)

    def mutate(root, info, id, nombre_comun, especie, edad_meses, altura_cm, frutos):
        for planta in plantas:
            if planta.id == id:
                planta.nombre_comun = nombre_comun
                planta.especie = especie
                planta.edad_meses = edad_meses
                planta.altura_cm = altura_cm
                planta.frutos = frutos
                return ActualizarPlanta(planta=planta)
        return None

class EliminarPlanta(Mutation):
    class Arguments:
        id = Int()

    planta = Field(Planta)

    def mutate(root, info, id):
        for i, planta in enumerate(plantas):
            if planta.id == id:
                plantas.pop(i)
                return EliminarPlanta(planta=planta)
        return None

class Mutations(ObjectType):
    crear_planta = CrearPlanta.Field()
    actualizar_planta = ActualizarPlanta.Field()
    eliminar_planta = EliminarPlanta.Field()

plantas = [
    Planta(
        id=1, nombre_comun="Cactus", especie="Cactaceae", edad_meses=12, altura_cm=20, frutos=False
    ),
    Planta(
        id=2, nombre_comun="Rosa", especie="Rosa", edad_meses=8, altura_cm=30, frutos=True
    ),
]

schema = Schema(query=Query, mutation=Mutations)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><head><title>GraphQL Server</title></head><body><h1>GraphQL Server is running!</h1></body></html>")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
