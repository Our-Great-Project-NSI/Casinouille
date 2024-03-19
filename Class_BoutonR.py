import pygame


class Bouton:
    def __init__(self, x, y, largeur, hauteur, texte, type_pari):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.texte = texte
        self.type_pari = type_pari
        self.font = pygame.font.Font(None, 24)

    def dessiner(self, ecran):
        pygame.draw.rect(ecran, (255, 255, 255), self.rect, 2)
        ecran.blit(self.font.render(self.texte, True, (255, 255, 255)), (self.rect.x, self.rect.y))

    def est_clique(self, position_souris):
        return self.rect.collidepoint(position_souris)
