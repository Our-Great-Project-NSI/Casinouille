import random


class Roulette:
    def __init__(self):
        self.rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.vert = [0]

    def spin(self):
        number = random.randint(0, 36)
        if number in self.rouge:
            color = 'Rouge'
        elif number in self.noir:
            color = 'Noir'
        else:
            color = 'Vert'
        return number, color
