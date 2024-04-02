# IMPORTS

import pygame
from pygame.locals import *
import sys

# INIT. PYGAME

pygame.init()
infoObject = pygame.display.Info()
size = (infoObject.current_w, infoObject.current_h)
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 64)
GAMEBG = pygame.image.load('grille.png')
bg_width = GAMEBG.get_width()
bg_height = GAMEBG.get_height()
scale_factor = WIDTH / bg_width
scaled_width = int(bg_width * scale_factor)
scaled_height = int(bg_height * scale_factor)
scaled_bg = pygame.transform.scale(GAMEBG, (scaled_width, scaled_height))

dico_pari = {(1,1):"",(1,2):"",(1,3):"",(1,4):"",(1,5):"",(1,6):"",(1,7):"",(1,8):"",(1,9):"",(1,10):"",(1,11):"",(1,12):"",
             (2,1):"",(2,2):"",(2,3):"",(2,4):"",(2,5):"",(2,6):"",(2,7):"",(2,8):"",(2,9):"",(2,10):"",(2,11):"",(2,12):"",
             (3,1):"",(3,2):"",(3,3):"",(3,4):"",(3,5):"",(3,6):"",(3,7):"",(3,8):"",(3,9):"",(3,10):"",(3,11):"",(3,12):"",}

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            screen.blit(scaled_bg, (WIDTH / 2 - scaled_width / 2, HEIGHT / 2 - scaled_height / 2))

    pygame.display.flip()

