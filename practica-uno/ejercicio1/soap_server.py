from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Define la función para las operaciones
def operaciones(a, b, operacion):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        if b == 0:
            return "Error: división por cero"
        else:
            return a / b
    else:
        return "Operación no válida"

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "operaciones-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# Registramos el servicio para las operaciones
dispatcher.register_function(
    "Operaciones",
    operaciones,
    returns={"resultado": int},
    args={"a": int, "b": int, "operacion": str},
)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
