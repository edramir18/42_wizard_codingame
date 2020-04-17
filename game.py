import sys
import math


class Entity:
    def __init__(self, arr):
        """

        :param list arr:
        """
        self.entity_id = int(arr[0])
        self.type = str(arr[1])
        self.x = int(arr[2])
        self.y = int(arr[3])
        self.vx = int(arr[4])
        self.vy = int(arr[5])
        self.state = int(arr[6])
        self.mass = 0
        self.radius = 0

    def distance(self, other):
        """

        :param Entity other: The entity to get the distance from
        :return: int: Distance to the entity
        """
        dist = (self.x - other.x) * (self.x - other.x)
        dist += (self.y - other.y) * (self.y - other.y)
        return dist


class Wizard(Entity):
    def __init__(self, arr, team_id, game):
        """

        :param list arr:
        :param int team_id:
        :param Game game:
        """
        super().__init__(arr)
        self.mass = 1.0
        self.radius = 400
        self.radius2 = 400 * 400
        self.team_id = team_id # type: int
        self.game = game

    def defend(self):
        if self.game.player.magic >= 50:
            m = min(self.game.snaffles,
                    key=lambda x: self.game.enemy.goal.distance(x))
            return self.spell(m.entity_id, self.game.enemy.goal.x,
                              self.game.enemy.goal.y, 34)
        if self.state == 1:
            return self.throw(self.game.enemy.goal.x, self.game.enemy.goal.y,
                              500)
        if self.team_id == 0:
            center = 2000
            s = [v for v in self.game.snaffles if v.x <= 4000]
        else:
            center = 14000
            s = [v for v in self.game.snaffles if v.x >= 12000]
        if len(s) > 0:
            m = min(s, key=lambda x: self.distance(x))
            return self.move(m.x, m.y, 120)
        return self.move(center, 3750, 150)

    def attack(self):
        if self.state == 1:
            return self.throw(self.game.enemy.goal.x, self.game.enemy.goal.y,
                              500)
        if self.team_id == 0:
            center = 14500
        else:
            center = 1500
        m = min(self.game.snaffles,
                key=lambda x: self.game.enemy.goal.distance(x))
        # m = min(s, key=lambda x: self.distance(x))
        return self.move(m.x, m.y, 150)

    @staticmethod
    def move(x, y, thrust):
        return f'MOVE {x} {y} {thrust}'

    @staticmethod
    def throw(x, y, power):
        return f'THROW {x} {y} {power}'

    @staticmethod
    def spell(entity_id, x, y, magic):
        return f'WINGARDIUM {entity_id} {x} {y} {magic}'


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

    def __init__(self, team_id, arr, goal):
        self.team_id = team_id # type: int
        self.score = arr[0] # type: int
        self.magic = arr[1] # type: int
        self.wizards = []  # type: list[Wizard]
        self.goal = goal  # type: Goal


class Game:
    """Class to store the information for all entities from a game turn"""

    def __init__(self, player, enemy):
        """

        :param Team player:
        :param Team enemy:
        """
        self.player = player  # type: Team
        self.enemy = enemy  # type: Team
        self.bludgers = []  # type: list[Bludger]
        self.snaffles = []  # type: list[Snaffle]


class Goal:
    def __init__(self, x, y):
        self.x = x  # type: int
        self.y = y  # type: int
        self.top_pole = y - 2000  # type: int
        self.bottom_pole = y + 2000  # type: int
        self.pole_radius = 300  # type: int

    def distance(self, other):
        """

        :param Entity other: The entity to get the distance from
        :return: int: Distance to the entity
        """
        dist = (self.x - other.x) * (self.x - other.x)
        dist += (self.y - other.y) * (self.y - other.y)
        return dist


p_team = int(input())
if p_team == 0:
    e_team = 1
    player_goal = Goal(0, 3750)
    enemy_goal = Goal(16000, 3750)
else:
    e_team = 0
    player_goal = Goal(16000, 3750)
    enemy_goal = Goal(0, 3750)

# game loop
while True:
    team1 = Team(p_team, [int(i) for i in input().split()], player_goal)
    team2 = Team(e_team, [int(i) for i in input().split()], enemy_goal)
    entities = int(input())  # number of entities still in game
    game_state = Game(team1, team2)
    for i in range(entities):
        entity = input().split()
        if entity[1] == 'WIZARD':
            game_state.player.wizards.append(Wizard(entity, p_team, game_state))
        elif entity[1] == 'BLUDGER':
            game_state.bludgers.append(Bludger(entity))
        elif entity[1] == 'SNAFFLE':
            game_state.snaffles.append(Snaffle(entity))
        else:
            game_state.enemy.wizards.append(Wizard(entity, e_team, game_state))
    print(game_state.player.wizards[0].defend())
    print(game_state.player.wizards[1].attack())
