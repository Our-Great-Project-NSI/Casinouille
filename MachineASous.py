# -*- coding: utf-8 -*-

# =============================================================================
#                            Machine à sous 
# =============================================================================
"""
Created on Tue Jan 16 14:02:08 2024

@author: hugolormier
ver: 1.0
"""
# ============================== Import =======================================
from random import shuffle,choice,random
from time import sleep
from Class_Machine import *
import pygame
import sys
from random import choice

# ============================== Initialisation ===============================

# On définie les variables (taille longueur - largeur) et fonds d'écrans
pygame.init()
infoObject = pygame.display.Info()
size = (infoObject.current_w, infoObject.current_h)
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 64)  
GAMEBG = pygame.image.load('backgroundblackjack2.png')
MACHINEBG = pygame.image.load('backgroundmachine2.png')
game_background = pygame.transform.scale(GAMEBG, (WIDTH, HEIGHT))
machine_background = pygame.transform.scale(MACHINEBG, (WIDTH/1.5, HEIGHT/1.5))

# Chargement des images objets dans la machine
banane = pygame.image.load('banane.png')
cerise = pygame.image.load('cerise.png')
pique = pygame.image.load('pique.png')
sept = pygame.image.load('sept.png')
diamant = pygame.image.load('diamant.png')
pomme = pygame.image.load('pomme.png')
carreau = pygame.image.load('carreau.png')
coin = pygame.image.load('coin.png')

# Chargement de la taille des images par rapport à l'écran
banane = pygame.transform.scale(banane, (WIDTH/10, HEIGHT/7))
cerise = pygame.transform.scale(cerise, (WIDTH/10, HEIGHT/7))
pique = pygame.transform.scale(pique, (WIDTH/10, HEIGHT/7))
sept = pygame.transform.scale(sept, (WIDTH/10, HEIGHT/7))
diamant = pygame.transform.scale(diamant, (WIDTH/10, HEIGHT/7))
pomme = pygame.transform.scale(pomme, (WIDTH/10, HEIGHT/7))
carreau = pygame.transform.scale(carreau, (WIDTH/10, HEIGHT/7))
coin = pygame.transform.scale(coin, (WIDTH/10, HEIGHT/7))

# listes qui définie les pourcentages de chance d'avoir tel ou tel objets
liste_objet = ["banane"] * 11 + ["cerise"] * 11 + ["pomme"] * 11 + ["pique"] * 5 + ["carreau"] * 5 + ["dollar"] * 5 + ["diamant"] * 2+ ["sept"] * 2   

# Créer un dictionnaire pour mapper les noms des objets à leurs images
objet_images = {'banane': banane, 'cerise': cerise, 'pique': pique, 'sept': sept, 'diamant': diamant, 'pomme':pomme, 'carreau': carreau, 'dollar': coin  }  

# Créer une liste pour stocker les objets actuels au lancement de la machine
current_objects = ['banane', 'cerise', 'banane']

# Création du bouton de lancement de la partie
button = Button(size[0] // 2 - HEIGHT/-3.8, size[1] - WIDTH/4.5 , WIDTH/10, HEIGHT/6)

# ============================ Les fonctions ==================================

def draw_slot_machine():
    """dessine la machine à sous : 
        le placement des images sur l'écran en x,y et leur espacement,
        le texte de victoire et de gains possible,
        le bouton de lancement."""
        
    # calcule la hauteur de l'image 
    total_height = 3 * banane.get_height() + 2 

    # calcule la positionde départ
    start_y = (size[1] - total_height) // 2

    # Dessine les objets images sur l'écran
    for i, objet in enumerate(current_objects):
        image = objet_images[objet]
        rect = image.get_rect()
        rect.center = (size[0] // 2.09, start_y + 1.4 * i * (image.get_height()) + HEIGHT/36)
        screen.blit(image, rect)

    # Ecrit le texte 'Win' ou 'Loose' quand la machine a fini de rouler
    if not rolling:
        if current_objects[0] == current_objects[1] == current_objects[2]:
            text = 'Win'
        else:
            text = 'Loose'
            
        text_surface = font.render(text, True, (255, 187, 0))
        rotated_text_surface = pygame.transform.rotate(text_surface, 90)  # Tourne le texte de 90 degrés
        text_rect = rotated_text_surface.get_rect()
        text_rect.center = (size[0] // 2 - WIDTH/4.3, size[1] - HEIGHT/2.1)
        screen.blit(rotated_text_surface, text_rect)  # Dessine le texte 
        button.draw(screen, alpha = 0)  # Dessine le bouton
rolling = False

# Ajoutez une variable pour suivre le temps depuis le dernier roll
last_roll_time = pygame.time.get_ticks() - 3001  

def roll_slot_machine():
    """Fonction qui fait rouler les images pour simuler la machine
    à sous, le for i in range définie le nombre d'image qui
    défille."""
    
    global rolling, last_roll_time
    if rolling:
        return
    rolling = True
    for _ in range(15):
        screen.blit(game_background, (0, 0))
        screen.blit(machine_background, (WIDTH/4.7, HEIGHT/5.5))
        current_objects[0] = choice(liste_objet)
        current_objects[1] = choice(liste_objet)
        current_objects[2] = choice(liste_objet)
        draw_slot_machine()
        pygame.display.flip()
        sleep(0.1)
    rolling = False
    last_roll_time = pygame.time.get_ticks()  # Mettez à jour le temps du dernier roll
    draw_slot_machine()  # Dessine la Machine 
    
# ========================= Branche principale ================================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Only roll the slot machine if the button is clicked and visible
            if pygame.time.get_ticks() - last_roll_time > 1000 and not rolling and button.is_clicked(event):
                roll_slot_machine()

    # If more than 3 seconds have passed since the last roll, display the button
    if pygame.time.get_ticks() - last_roll_time > 1000 and not rolling:
        screen.blit(game_background, (0, 0))
        screen.blit(machine_background, (WIDTH/4.7, HEIGHT/5.5))
        draw_slot_machine()
    pygame.display.flip()