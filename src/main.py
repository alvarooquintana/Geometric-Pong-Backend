from fastapi import FastAPI, WebSocket
import random

app = FastAPI()

from game_manager import GameManager
game_manager = GameManager()

class SessionManager:
    
    def __init__(self):
        self.sessions = []
    
    def add_session(self,player_id,ws):
        self.sessions.append(Session(player_id,ws))

        
class Session:
    
    def __init__(self,player_id,ws):
        self.player_id = player_id 
        self.ws = ws

class RoomManager:
    def __init__(self):
        self.room = []

    def add_room(self, player_id,ws):
        self.room.append(Room(player_id,ws))

    def 

class Room:
    def __init__(self,player_id,ws):
        self.player_id = player_id
        self.ws = ws

room_manager = RoomManager()

session_manager = SessionManager()


@app.get('/')
async def get():
    return 'Hola'


@app.websocket("/play")
async def job_status_websocket(websocket: WebSocket):
    
    await websocket.accept()
    player_id = random.randint(1,1000)
    session_manager.add_session(player_id,websocket)
    
    print(session_manager.sessions)

 
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

            elif data.get("msg") == "ready":
                pass

        except Exception as e:
            print(e)
            await websocket.send_json({'msg': str(e)})






