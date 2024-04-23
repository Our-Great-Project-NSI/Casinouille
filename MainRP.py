# IMPORTS

import pygame
from pygame.locals import *
import sys
from Class_Roulette import *
from Class_Portefeuille import *
from Class_PariR import *

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

# INIT. VARIABLES

button_width = WIDTH / 15.6
button_height = HEIGHT / 5.5
debut_button_x = WIDTH / 6.8
debut_button_y = HEIGHT / 7.8

button2_width = WIDTH / 4
button2_height = HEIGHT / 10.5
debut_button2_x = WIDTH / 6.8
debut_button2_y = HEIGHT / 1.47

button3_width = WIDTH / 8
button3_height = HEIGHT / 10.5
debut_button3_x = WIDTH / 6.8
debut_button3_y = HEIGHT / 1.28

b2 = Button(debut_button3_x, debut_button3_y, button3_width, button3_height, color=(255, 255, 255))

dico_pari = {(1, -2): 0, (1, -1): 0, (1, 0): 0, (1, 1): 3, (1, 2): 6, (1, 3): 9, (1, 4): 12, (1, 5): 15, (1, 6): 18,
             (1, 7): 21,
             (1, 8): 24, (1, 9): 27,
             (1, 10): 30, (1, 11): 33, (1, 12): 36, (1, 13): "L1", (1, 14): "L1",
             (2, -2): 0, (2, -1): 0, (2, 0): 0, (2, 1): 2, (2, 2): 5, (2, 3): 8, (2, 4): 11, (2, 5): 14, (2, 6): 17,
             (2, 7): 20,
             (2, 8): 23, (2, 9): 26,
             (2, 10): 29, (2, 11): 32, (2, 12): 35, (2, 13): "L2", (2, 14): "L2",
             (3, -2): 0, (3, -1): 0, (3, 0): 0, (3, 1): 1, (3, 2): 4, (3, 3): 7, (3, 4): 10, (3, 5): 13, (3, 6): 16,
             (3, 7): 19,
             (3, 8): 22, (3, 9): 25,
             (3, 10): 28, (3, 11): 31, (3, 12): 34, (3, 13): "L3", (3, 14): "L3"}

dico_pari2 = {(1, 1): 1, (1, 2): 2, (1, 3): 3}

dico_pari3 = {(1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4, (1, 5): 5, (1, 6): 6}

# CREA. INSTANCES P.O.O.
roulette = Roulette()
portefeuille = Portefeuille(1000)  # Commence avec 1000 euros
pari = Pari(roulette, portefeuille)
# MAIN

while True:
    b2.draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cx = int((x - debut_button_x) // button_width + 1)
            cy = int((y - debut_button_y) // button_height + 1)
            cx2 = int((x - debut_button2_x) // button2_width + 1)
            cy2 = int((y - debut_button2_y) // button2_height + 1)
            cx3 = int((x - debut_button3_x) // button3_width + 1)
            cy3 = int((y - debut_button3_y) // button3_height + 1)
            if (cy, cx) in dico_pari:
                print(f'{dico_pari[(cy, cx)]}')
                if type(dico_pari[(cy, cx)]) == int:
                    nombre = int(dico_pari[(cy, cx)])
                    mise = 10  # A MODIFIER
                    pari_gagne, gain = pari.parier('parier_nombre', mise, nombre)
                    if pari_gagne:
                        print(
                            f'Félicitations ! Vous avez gagné le pari sur le nombre {nombre}. Votre gain est de {gain} euros.')
                        print(f'Votre solde est de : {portefeuille.solde}')
                    else:
                        print(f'Malheureusement, vous avez perdu le pari sur le nombre {nombre}.')
                        print(f'Votre solde est de : {portefeuille.solde}')
                elif type(dico_pari[(cy, cx)]) == str:
                    if dico_pari[(cy, cx)] in ['L1', 'L2', 'L3']:
                        ligne = dico_pari[(cy, cx)]
                        mise = 10  # A MODIFIER
                        pari_gagne, gain = pari.parier('parier_ligne', mise, ligne)
                        if pari_gagne:
                            print(
                                f'Félicitations ! Vous avez gagné le pari sur la ligne n°{ligne}. Votre gain est de {gain} euros.')
                            print(f'Votre solde est de : {portefeuille.solde}')
                        else:
                            print(f'Malheureusement, vous avez perdu le pari sur la ligne n°{ligne}.')
                            print(f'Votre solde est de : {portefeuille.solde}')
            elif (cy2, cx2) in dico_pari2:
                douz = dico_pari2[(cy2, cx2)]
                mise = 10  # A MODIFIER
                pari_gagne, gain = pari.parier('parier_douzaine', mise, douz)
                if pari_gagne:
                    print(
                        f'Félicitations ! Vous avez gagné le pari sur la douzaine n°{douz}. Votre gain est de {gain} euros.')
                    print(f'Votre solde est de : {portefeuille.solde}')
                else:
                    print(f'Malheureusement, vous avez perdu le pari sur la douzaine n°{douz}.')
                    print(f'Votre solde est de : {portefeuille.solde}')
            elif (cy3, cx3) in dico_pari3:
                if dico_pari3[(cy3, cx3)] in [1, 6]:  # CASE 18AINES
                    if dico_pari3[(cy3, cx3)] == 1:
                        dixhuit = 1
                        mise = 10  # A MODIFIER
                        pari_gagne, gain = pari.parier('parier_dixhuit', mise, dixhuit)
                        if pari_gagne:
                            print(
                                f'Félicitations ! Vous avez gagné le pari sur les nombres de 1 à 18. Votre gain est de {gain} euros.')
                            print(f'Votre solde est de : {portefeuille.solde}')
                        else:
                            print('Malheureusement, vous avez perdu le pari sur les nombres de 1 à 18.')
                            print(f'Votre solde est de : {portefeuille.solde}')
                    else:
                        dixhuit = 2
                        mise = 10  # A MODIFIER
                        pari_gagne, gain = pari.parier('parier_dixhuit', mise, dixhuit)
                        if pari_gagne:
                            print(
                                f'Félicitations ! Vous avez gagné le pari sur les nombres de 19 à 36. Votre gain est de {gain} euros.')
                            print(f'Votre solde est de : {portefeuille.solde}')
                        else:
                            print('Malheureusement, vous avez perdu le pari sur les nombres de 19 à 36.')
                            print(f'Votre solde est de : {portefeuille.solde}')
                if dico_pari3[(cy3, cx3)] in [2, 5]:  # CASE PAIR / IMPAIR
                    if dico_pari3[(cy3, cx3)] == 2:
                        p_type = "pair"
                    else:
                        p_type = "impair"
                    mise = 10  # A MODIFIER
                    pari_gagne, gain = pari.parier('parier_pair_impair', mise, p_type)
                    if pari_gagne:
                        print(
                            f'Félicitations ! Vous avez gagné le pari sur les nombres {p_type}. Votre gain est de {gain} euros.')
                        print(f'Votre solde est de : {portefeuille.solde}')
                    else:
                        print(f'Malheureusement, vous avez perdu le pari sur les nombres {p_type}.')
                        print(f'Votre solde est de : {portefeuille.solde}')
                if dico_pari3[(cy3, cx3)] in [3, 4]:  # CASE ROUGE / NOIR
                    if dico_pari3[(cy3, cx3)] == 3:
                        couleur = 'Rouge'
                    else:
                        couleur = 'Noir'
                    mise = 10  # A MODIFIER
                    pari_gagne, gain = pari.parier('parier_couleur', mise, couleur)
                    if pari_gagne:
                        print(
                            f'Félicitations ! Vous avez gagné le pari la couleur {couleur}. Votre gain est de {gain} euros.')
                        print(f'Votre solde est de : {portefeuille.solde}')
                    else:
                        print(f'Malheureusement, vous avez perdu le pari sur la couleur {couleur}.')
                        print(f'Votre solde est de : {portefeuille.solde}')

        screen.blit(scaled_bg, (WIDTH / 2 - scaled_width / 2, HEIGHT / 2 - scaled_height / 2))

    pygame.display.flip()

