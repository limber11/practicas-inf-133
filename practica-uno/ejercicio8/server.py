from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CaesarCipher:
    @staticmethod
    def encrypt_message(message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shifted = ord(char) + 3
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                encrypted_message += chr(shifted)
            else:
                encrypted_message += char
        return encrypted_message

class Message:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.encrypted_content = CaesarCipher.encrypt_message(content)

class MessageStorage:
    def __init__(self):
        self.messages = {}
        self.next_id = 1

    def create_message(self, content):
        message_id = self.next_id
        self.messages[message_id] = Message(message_id, content)
        self.next_id += 1
        return message_id

    def get_all_messages(self):
        return list(self.messages.values())

    def get_message_by_id(self, message_id):
        return self.messages.get(message_id)

    def update_message_content(self, message_id, new_content):
        if message_id in self.messages:
            self.messages[message_id].content = new_content
            self.messages[message_id].encrypted_content = CaesarCipher.encrypt_message(new_content)
            return True
        return False

    def delete_message(self, message_id):
        if message_id in self.messages:
            del self.messages[message_id]
            return True
        return False

class MessageRequestHandler(BaseHTTPRequestHandler):
    storage = MessageStorage()

    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/mensajes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            content = request_data.get("contenido")
            if content:
                message_id = self.storage.create_message(content)
                response_data = {"message": "Mensaje creado", "id": message_id}
                self.response_handler(201, response_data)
            else:
                self.response_handler(400, {"error": "El contenido del mensaje es requerido"})
        else:
            self.response_handler(404, {"error": "Ruta no encontrada"})

    def do_GET(self):
        if self.path == "/mensajes":
            messages = [{"id": message.id, "contenido": message.content, "contenido_encriptado": message.encrypted_content} for message in self.storage.get_all_messages()]
            self.response_handler(200, messages)
        elif self.path.startswith("/mensajes/"):
            message_id = int(self.path.split("/")[-1])
            message = self.storage.get_message_by_id(message_id)
            if message:
                message_data = {"id": message.id, "contenido": message.content, "contenido_encriptado": message.encrypted_content}
                self.response_handler(200, message_data)
            else:
                self.response_handler(404, {"error": "Mensaje no encontrado"})
        else:
            self.response_handler(404, {"error": "Ruta no encontrada"})

    def do_PUT(self):
        if self.path.startswith("/mensajes/"):
            message_id = int(self.path.split("/")[-1])
            content_length = int(self.headers["Content-Length"])
            put_data = self.rfile.read(content_length)
            request_data = json.loads(put_data.decode("utf-8"))

            new_content = request_data.get("contenido")
            if new_content:
                if self.storage.update_message_content(message_id, new_content):
                    self.response_handler(200, {"message": "Contenido del mensaje actualizado"})
                else:
                    self.response_handler(404, {"error": "Mensaje no encontrado"})
            else:
                self.response_handler(400, {"error": "El contenido del mensaje es requerido"})
        else:
            self.response_handler(404, {"error": "Ruta no encontrada"})

    def do_DELETE(self):
        if self.path.startswith("/mensajes/"):
            message_id = int(self.path.split("/")[-1])
            if self.storage.delete_message(message_id):
                self.response_handler(200, {"message": "Mensaje eliminado"})
            else:
                self.response_handler(404, {"error": "Mensaje no encontrado"})
        else:
            self.response_handler(404, {"error": "Ruta no encontrada"})

def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, MessageRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()
