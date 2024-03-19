import pygame
import sys


class Interface:
    def __init__(self, pari):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.pari = pari
        self.boutons = []
        self.creer_boutons()
        self.image_fond = pygame.image.load('UploadedImage2.jpg')

    def creer_boutons(self):
        # Créez ici les boutons pour chaque type de pari
        # Par exemple, pour le pari sur le rouge :
        self.boutons.append(Bouton(100, 100, 50, 50, "Rouge", "parier_couleur"))
        # Ajoutez plus de boutons ici...

    def dessiner_ecran(self):
        self.screen.blit(self.image_fond, (0, 0))
        for bouton in self.boutons:
            bouton.dessiner(self.screen)

    def mettre_a_jour(self):
        self.dessiner_ecran()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position_souris = pygame.mouse.get_pos()
                for bouton in self.boutons:
                    if bouton.est_clique(position_souris):
                        print(f"Vous avez cliqué sur le bouton {bouton.texte}!")
                        # Ici, vous pouvez appeler la méthode de pari correspondante de l'objet pari
                        # Par exemple : self.pari.parier(bouton.type_pari, montant_pari, valeur_pari)
        pygame.display.flip()
