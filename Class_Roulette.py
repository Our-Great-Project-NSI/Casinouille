import random
import pygame


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
        print('---')
        print(number, color)
        print('---')
        return number, color


class Button:
    def __init__(self, x, y, width, height, text=None, color=(0, 255, 0), font_size=36):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen, alpha=256):
        button_surface = pygame.Surface((self.rect.width, self.rect.height))
        button_surface.fill(self.color)
        button_surface.set_alpha(alpha)
        screen.blit(button_surface, (self.rect.x, self.rect.y))

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) / 2
        text_y = self.rect.y + (self.rect.height - text_surface.get_height()) / 2
        screen.blit(text_surface, (text_x, text_y))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
