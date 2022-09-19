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
class Person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

class Player(Person):
    def __init__(self, speed, agility, strenght):
        self.speed = speed
        self.agility = agility
        self.strenght = strenght

    def __str__(self):
        return f"{self.name} - other text"

class Coach(Person):
    def __init__(self, voice_level):
        self.voice_level = voice_level

    def __str__(self):
        return f"{self.name} - other text"

class Team:
    def __init__(self):
        self.players = []
        self.coach = None

    def add_player(self, player):
        self.players.append(player)

    def switch_coach(self, coach):
        self.coach = coach

bajen = Team()

bajen.switch_coach(Coach("Kennedy"))

print(Team.coach)