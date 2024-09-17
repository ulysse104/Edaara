from django.db import models
from .formation import Formation

class ModuleFormation(models.Model):
	titre_module = models.CharField(max_length=200)
	description_module = models.CharField(max_length=500)
	formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='modules')
	

	def __str__(self):
		return f'{self.titre_module}'

	#def affichage_apprenants_domaine(self)
	#	apprenants = self.apprenant_domaine.all()
	#	return ", ".join([apprenant.nom for apprenant in apprenants])

