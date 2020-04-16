import sys
import math


class Entity:
    def __init__(self, arr):
        """

        :param list arr:
        """
        self.id = int(arr[0])
        self.type = str(arr[1])
        self.x = int(arr[2])
        self.y = int(arr[3])
        self.vx = int(arr[4])
        self.vy = int(arr[5])
        self.state = int(arr[6])
        self.mass = 0
        self.radius = 0


class Wizard(Entity):
    def __init__(self, arr):
        """

        :param list arr:
        """
        super().__init__(arr)
        self.mass = 1.0
        self.radius = 400


class Snaffle(Entity):
    def __init__(self, arr):
        """

        :param list arr:
        """
        super().__init__(arr)
        self.mass = 0.5
        self.radius = 150


class Bludger(Entity):
    def __init__(self, arr):
        """

        :param list arr:
        """
        super().__init__(arr)
        self.mass = 8.0
        self.radius = 200


class Team:
    """Class to store information about a team"""
    def __init__(self, arr):
        self.score = arr[0]
        self.magic = arr[1]
        self.wizards = []       # type: list[Wizard]


class Game:
    """Class to store the information for all entities from a game turn"""
    def __init__(self, player, enemy):
        """

        :param Team player:
        :param Team enemy:
        """
        self.player = player    # type: Team
        self.enemy = enemy      # type: Team
        self.bludgers = []      # type: list[Bludger]
        self.snaffles = []      # type: list[Snaffle]


my_team_id = int(input())

# game loop
while True:
    team1 = Team([int(i) for i in input().split()])
    team2 = Team([int(i) for i in input().split()])
    entities = int(input())  # number of entities still in game
    game = Game(team1, team2)
    for i in range(entities):
        entity = input().split()
        if entity[1] == 'WIZARD':
            game.player.wizards.append(Wizard(entity))
        elif entity[1] == 'BLUDGER':
            game.bludgers.append(Bludger(entity))
        elif entity[1] == 'SNAFFLE':
            game.snaffles.append(Snaffle(entity))
        else:
            game.enemy.wizards.append(Wizard(entity))
    for wizard in game.player.wizards:
        print("MOVE 8000 3750 100")