from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random

class Game:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.games = []
        return cls._instance

    def create_game(self, element):
        game_id = len(self.games) + 1
        server_element = random.choice(["piedra", "papel", "tijera"])
        result = determine_winner(element, server_element)
        game_data = {
            "id": game_id,
            "elemento": element,
            "elemento_servidor": server_element,
            "resultado": result
        }
        self.games.append(game_data)
        return game_data

    def list_games(self):
        return self.games

    def list_games_by_result(self, result):
        return [game for game in self.games if game["resultado"] == result]

def determine_winner(player_element, server_element):
    if player_element == server_element:
        return "empató"
    elif (player_element == "piedra" and server_element == "tijera") or \
         (player_element == "tijera" and server_element == "papel") or \
         (player_element == "papel" and server_element == "piedra"):
        return "ganó"
    else:
        return "perdió"

class PlayerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/partidas":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if "resultado" in self.path:
                result = self.path.split("=")[1]
                game_data = json.dumps(game.list_games_by_result(result))
            else:
                game_data = json.dumps(game.list_games())
            self.wfile.write(game_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/partidas":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            element = json.loads(post_data.decode("utf-8"))["elemento"]
            game_data = game.create_game(element)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(game_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    global game
    game = Game()

    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, PlayerHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()
