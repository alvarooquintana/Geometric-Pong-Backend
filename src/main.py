from fastapi import FastAPI, WebSocket
import random
from game_manager import Game
app = FastAPI()


class SessionManager:

    def __init__(self):
        self.sessions = []

    def add_session(self, player_id, ws):
        self.sessions.append(Session(player_id, ws))


class Session:

    def __init__(self, player_id, ws):
        self.player_id = player_id
        self.ws = ws


class RoomsManager:
    def __init__(self):
        self.rooms = []

    def add_to_rooms(self, player):
        for room in self.rooms:
            if len(room.players) >= 2:
                new_room.enter_room(player)
            else:
                return player.append(room)

    def delete_room(self, players):
        self.rooms.remove(players)


class Room:
    def __init__(self):
        self.players = []

    def enter_room(self, player):
        self.players.append(player)

    def start_game(self):
        self.game = Game(self.players)
        self.game.run()
        
        

    def leave_room(self,player):
        pass
        

new_room = Room()
room_manager = RoomsManager()
session_manager = SessionManager()


@app.get('/')
async def get():
    return 'Hola'


@app.websocket("/play")
async def job_status_websocket(websocket: WebSocket):

    await websocket.accept()
    player_id = random.randint(1, 1000)
    # session_manager.add_session(Session)


    while True:
        try:
            data = await websocket.receive_json()

            if data.get("msg") == "name":
                await websocket.send_json({"msg": f'Hola, {data.get("name")}'})

            elif data.get("msg") == "ping":
                await websocket.send_json({"msg": "pong"})

            # Responde a todos los usuarios
            elif data.get("msg") == "all":
                for session in session_manager.sessions:
                    await session.ws.send_json({"hola": "chicos"})

            # elif data.get("msg") == "join":
                # await room_manager.add_room

        except Exception as e:
            print(e)
            await websocket.send_json({'msg': str(e)})
