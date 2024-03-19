import pygame
import sys


class Interface:
    def __init__(self, pari):
        self.pari = pari
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)

    def draw_screen(self):
        self.screen.fill((0, 0, 0))  # Remplit l'écran de noir
        # Ajoutez ici le code pour dessiner l'interface utilisateur

    def update(self):
        # Met à jour l'affichage et gère les événements
        self.draw_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

    # Ajoutez ici d'autres méthodes pour gérer les paris et les interactions de l'utilisateur
