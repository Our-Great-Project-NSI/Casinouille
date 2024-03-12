class Portefeuille:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def ajouter(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

