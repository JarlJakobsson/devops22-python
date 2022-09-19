# class Square:

#     def __init__(self, side):
#         self.side = side

#     # function arguments
#     def area(self):
#         square_area = self.side ** 2
#         return square_area
    
#     def circumfarance(self):
#         square_circumference = self.side * 4
#         return square_circumference

# my_square = Square(2)

# #print(my_square.area(), my_square.circumfarance())

# my_square2 = Square(3.5)

#print(my_square2.area(), my_square2.circumfarance())

#4
# from math import pi

# class Circle:
#     def __init__(self, radie, color = "Gray"):
#         self.radie = radie
    
#     def area(self):
#         cricle_area = (self.radie ** 2) * pi
#         return cricle_area
    
#     def circumference(self):
#         circle_circumference = 2 * pi * self.radie
#         return circle_circumference

# my_circle = Circle(5)

#print(my_circle.area(), my_circle.circumference())

#5
from random import randint

class Person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

class Player(Person):
    def __init__(self, name, birth, stats):
        super().__init__(name, birth)
        self.stats = stats

    def __str__(self):
        return f"{self.name} [{self.birth}] - {self.stats}"

class Coach(Person):
    def __init__(self, name, birth, voice_level):
        super().__init__(name, birth)
        self.voice_level = voice_level

    def __str__(self):
        return self.name

class Team:
    def __init__(self, players, coach):
        self.players = players
        self.coach = coach

    def create_team(self):
        team = f"Coach {self.coach}\n"
        team += "-------------- Players --------------\n"
        team += "\n".join(map(str, self.players))
        return team

def get_birth():
    birth = randint(1989, 2003)
    return birth

def get_voice():
    voice = randint(1, 10)
    return voice

def get_stats():
    stats = f'Speed: {randint(1,10)} Agility: {randint(1,10)} Strenght: {randint(1,10)}'
    return stats

def main():
    coach = Coach("Håkan",get_birth, get_voice())
    players = []

    for each in ["Mats", "Tom", "Hendrik", "Thigo", "Adem"]:
        birth = get_birth()
        players.append(Player(each, birth, get_stats()))

    team = Team(players, coach)
    print(team.create_team())
    return

if __name__ == '__main__':
    main()
