from Class_Portefeuille import *
from Class_Roulette import *
from Class_PariR import *

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)

# Définition de la taille de l'écran
TAILLE_ECRAN = (800, 600)
ecran = pygame.display.set_mode(TAILLE_ECRAN)

# Création d'une horloge pour contrôler le taux de rafraîchissement
horloge = pygame.time.Clock()

# Création des instances de vos classes
roulette = Roulette()
portefeuille = Portefeuille(1000)  # Commence avec 1000 euros
pari = Pari(roulette, portefeuille)

# Création des boutons de pari
types_pari = ['parier_couleur', 'parier_nombre', 'parier_plage', 'parier_douzaine', 'parier_colonne', 'parier_pair_impair', 'parier_manque_passe']
boutons_pari = {type_pari: pygame.Rect(20, 80 + i * 60, 200, 50) for i, type_pari in enumerate(types_pari)}

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for type_pari, rect in boutons_pari.items():
                if rect.collidepoint(event.pos):
                    # L'utilisateur a cliqué sur un bouton de pari
                    mise = 10  # À remplacer par la mise choisie par l'utilisateur
                    valeur = 'Rouge'  # À remplacer par la valeur choisie par l'utilisateur
                    gagne, gain = pari.parier(type_pari, mise, valeur)
                    print(f"Gagné: {gagne}, Gain: {gain}, Solde: {portefeuille.solde}")

    # Remplissage de l'écran
    ecran.fill((255, 255, 255))

    # Affichage du solde actuel
    police = pygame.font.Font(None, 36)
    texte = police.render(f"Solde actuel: {portefeuille.solde}", 1, (10, 10, 10))
    ecran.blit(texte, (20, 50))

    # Affichage des boutons de pari
    for type_pari, rect in boutons_pari.items():
        pygame.draw.rect(ecran, NOIR, rect, 2)
        texte = police.render(type_pari, 1, NOIR)
        ecran.blit(texte, rect.move(10, 10))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Contrôle du taux de rafraîchissement
    horloge.tick(60)
