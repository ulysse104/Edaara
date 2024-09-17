from django.db import models
#from User_gestion.models.apprenant import Apprenant

class Domaine(models.Model):
	domaine = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.domaine}'

	#def affichage_apprenants_domaine(self)
	#	apprenants = self.apprenant_domaine.all()
	#	return ", ".join([apprenant.nom for apprenant in apprenants])

