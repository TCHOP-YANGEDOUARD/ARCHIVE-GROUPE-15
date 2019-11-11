# coding:utf-8

class Gestionnaire:

    def __init__(self, emprunt, compte):
        self.emprunt = emprunt
        self.compte = compte

    def ajout(self, compte):
        print("le compte ajouté est {}".format(self.compte))

    def modifier(self, compte):
        print("le compte modifier est {}".format(self.compte))

    def suppression(self, compte):
        print("le compte {} est supprimé avec succès".format(self.compte))

    def enregistrer(self, emprunt):
        if self.emprunt == 0:
            print("Le client n'a pas de dêtte")
        else:
            print("Le client a un emprunt")


g1 = Gestionnaire(10000, 50000)
g1.ajout("le premier compte est:")
g1.enregistrer("emprunt enregistrer")

g2 = Gestionnaire(0, 100000)
g2.modifier("compte modifier")
g2.enregistrer("emprunt enregistrer")
g2.suppression("supprimer compte")
