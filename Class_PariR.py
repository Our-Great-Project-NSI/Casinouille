class Pari:
    def __init__(self, roulette, portefeuille):
        self.roulette = roulette
        self.portefeuille = portefeuille

    def parier(self, type_pari, mise, valeur):
        self.portefeuille.retirer(mise)
        if getattr(self, type_pari)(valeur):
            gain = self.calculer_gain(type_pari, mise)
            self.portefeuille.ajouter(gain)
            return True, gain
        else:
            return False, 0

    def calculer_gain(self, type_pari, mise):
        if type_pari in ['parier_couleur', 'parier_pair_impair']:
            return mise * 2
        elif type_pari == 'parier_nombre':
            return mise * 36
        elif type_pari in ['parier_douzaine', 'parier_ligne']:
            return mise * 3
        elif type_pari == 'parier_dixhuit':
            return mise * 2

    def parier_couleur(self, couleur):
        _, couleur_gagnante = self.roulette.spin()
        return couleur == couleur_gagnante

    def parier_nombre(self, nombre):
        nombre_gagnant, _ = self.roulette.spin()
        return nombre == nombre_gagnant

    def parier_dixhuit(self, dixhuit_c):
        nombre_gagnant, _ = self.roulette.spin()
        diz1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        diz2 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        if nombre_gagnant in diz1:
            diz_g = 1
        elif nombre_gagnant in diz2:
            diz_g = 2
        else:
            diz_g = 0
        return dixhuit_c == diz_g

    def parier_douzaine(self, douz_c):
        nombre_gagnant, _ = self.roulette.spin()
        douz1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        douz2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        douz3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        if nombre_gagnant in douz1:
            douz_g = 1
        elif nombre_gagnant in douz2:
            douz_g = 2
        elif nombre_gagnant in douz3:
            douz_g = 3
        else:
            douz_g = 0
        return douz_c == douz_g

    def parier_ligne(self, ligne_choisie):
        nombre_gagnant, _ = self.roulette.spin()
        L1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        L2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        L3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        if nombre_gagnant in L1:
            l_gagnant = "L1"
        elif nombre_gagnant in L2:
            l_gagnant = "L2"
        elif nombre_gagnant in L3:
            l_gagnant = "L3"
        else:
            l_gagnant = "0"
        return ligne_choisie == l_gagnant

    def parier_pair_impair(self, p_type):
        nombre_gagnant, _ = self.roulette.spin()
        rg = nombre_gagnant%2
        if p_type == "pair" and rg == 0:
            return True
        else:
            return False


