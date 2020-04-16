import sys
import math


class Entity:
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        self.id = int(entity_id)
        self.type = entity_type
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)
        self.state = int(state)
        self.mass = 0
        self.radius = 0


class Wizard(Entity):
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        super().__init__(entity_id, entity_type, x, y, vx, vy, state)
        self.mass = 1
        self.radius = 400


class Snaffles(Entity):
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        super().__init__(entity_id, entity_type, x, y, vx, vy, state)
        self.mass = 0.5
        self.radius = 150


class Bludgers(Entity):
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        super().__init__(entity_id, entity_type, x, y, vx, vy, state)
        self.mass = 8
        self.radius = 200


class Team:
    def __init__(self, score, magic):
        self.score = score
        self.magic = magic
        self.wizards = []


class Game:
    def __init__(self, player, enemy, bludgers, snaffles):
        self.player = player
        self.enemy = enemy
        self.bludgers = bludgers
        self.snaffles = snaffles


my_team_id = int(input())

# game loop
while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    for i in range(entities):
        v1, v2, v3, v4, v5, v6, v7 = input().split()
        entity = Entity(v1, v2, v3, v4, v5, v6, v7)
    for i in range(2):
        print("MOVE 8000 3750 100")