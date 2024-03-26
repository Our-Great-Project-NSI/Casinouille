# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:00:34 2024

@author: hugolormier
"""

from random import shuffle,choice,random
import pygame
liste_objet = ["banane"] * 11 + ["cerise"] * 11 + ["pomme"] * 11 + ["pique"] * 5 + ["carreau"] * 5 + ["dollar"] * 5 + ["diamant"] * 2+ ["sept"] * 2

class Objet:    
    def __init__(self,objet):
        self.objet = objet
    
    def __str__(self):
        """personnalise la fonction print"""
        return(" | " +str(self.objet)+ " | ")
    
    def __eq__(self, other):
        if isinstance(other, Objet):
            return self.objet == other.objet
        return False
        
    def Affiche_Objet(self):
        """affiche une carte"""
        print("| ",self.objet, " | ")
        
    #accesseurs
    def get_objet(self):
        """renvoie la couleur de la carte"""
        return(self.objet)
    
    #mutateurs
    def set_objet(self,nouveau):
        """change la couleur de la carte"""
        self.objet = nouveau


class Machine:
    """classe d'une machine à sous"""
    def __init__(self):
        self.partie = []
        for i in range(0,3):
            self.partie.append(Objet(choice(liste_objet)))
        shuffle(self.partie)    
    
    def Affiche_Roll(self):
        """Affiche le résultat d'une partie"""
        for elt1 in self.partie :
            elt1.Affiche_Objet()
        # verifie si le roll à 3 objet similaire
        if self.partie[0] == self.partie[1] and self.partie[0] == self.partie[2]:
            print("Win")
        else: 
            print("Loose")
       
            
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
            
        