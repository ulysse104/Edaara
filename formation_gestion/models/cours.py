from django.db import models
from .module import ModuleFormation

class Cours(models.Model):
	titre_cours = models.CharField(max_length=200)
	cours_module = models.ForeignKey(ModuleFormation, on_delete=models.CASCADE, related_name='module_cours')
	


	def __str__(self):
		return f'{self.titre_cours}'

	#def affichage_apprenants_domaine(self)
	#	apprenants = self.apprenant_domaine.all()
	#	return ", ".join([apprenant.nom for apprenant in apprenants])

