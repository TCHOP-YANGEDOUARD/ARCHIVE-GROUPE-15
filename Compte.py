#coding:idf-8
class Compte:
	
	def __init__(self,solde):
		
		self.solde=solde
class Epargne(Compte):
	
	def afficher(self):
			
	print("Votre solde du compte d'épargne est : ",self.solde)

class Courant(Compte):
	def afficher(self):
			
print("Votre solde d& u compte courant est : ",self.solde)


ep=Epargne(10000)
cc=Courant(50000)
ep.afficher()
cc.afficher()
