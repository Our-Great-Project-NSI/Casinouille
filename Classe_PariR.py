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
        if type_pari in ['parier_couleur', 'parier_pair_impair', 'parier_manque_passe']:
            return mise * 2
        elif type_pari == 'parier_nombre':
            return mise * 36
        elif type_pari in ['parier_douzaine', 'parier_colonne']:
            return mise * 3
        elif type_pari == 'parier_plage':
            return mise * 2

    def parier_couleur(self, couleur):
        _, couleur_gagnante = self.roulette.spin()
        return couleur == couleur_gagnante

    def parier_nombre(self, nombre):
        nombre_gagnant, _ = self.roulette.spin()
        return nombre == nombre_gagnant

    def parier_plage(self, plage):
        nombre_gagnant, _ = self.roulette.spin()
        return plage[0] <= nombre_gagnant <= plage[1]

    def parier_douzaine(self, douzaine):
        nombre_gagnant, _ = self.roulette.spin()
        return 12 * (douzaine - 1) < nombre_gagnant <= 12 * douzaine

    def parier_colonne(self, colonne):
        nombre_gagnant, _ = self.roulette.spin()
        return nombre_gagnant % 3 == colonne - 1

    def parier_pair_impair(self, pari):
        nombre_gagnant, _ = self.roulette.spin()
        return (nombre_gagnant % 2 == 0) if pari == 'pair' else (nombre_gagnant % 2 == 1)

    def parier_manque_passe(self, pari):
        nombre_gagnant, _ = self.roulette.spin()
        return (1 <= nombre_gagnant <= 18) if pari == 'manque' else (19 <= nombre_gagnant <= 36)

