import uuid
import pygame

class GameManager:
    def __init__(self):
        self.games = []

    def create_game(self, players):
        self.games.append(Game(players))


class Player:
    def __init__(self, x, y, w, h, lifes, speed, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.w = w or 50
        self.h = h or 10
        self.dx = dx
        self.dy = dy
        self.lifes = lifes or 2
        self.speed = speed or 25
        self.color = color or [201, 245, 230]


class Ball:
    def __init__(self, x, y, radius, dx, dy, speed, color):
        self.id = uuid.uuid4()
        self.x = x or 135
        self.y = y or 195
        self.radius = radius or 10
        self.dx = dx or -60
        self.dy = dy or -60
        self.speed = speed or False 
        self.color = color or [121, 168, 50]


class Game:
    def __init__(self, players):
        self.id = uuid.uuid4()

        self.players = players
        self.balls = []

        self.x = 300
        self.y = 450
        self.lastDraw = 0

        self.winner = False
        self.running = False

        self.clock = None

    def run(self):
        self.clock = pygame.time.Clock()
        self.running = True
        
        while self.running:
            dt = self.clock.tick(60)
            self.handle_events(dt)
            self.update_positions(dt)


    
    def tick(self):
        pass

    def stop(self):
        pass


