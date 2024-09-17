from django.db import models
from .cours import Cours

class Chapitre(models.Model):
	titre = models.CharField(max_length=200)
	details = models.TextField()
	cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='chapitre')
		

	def __str__(self):
		return f'{self.titre}'

	def modifier_titre(self,nouveau_titre, nouveau_details):
		
		self.titre = nouveau_titre
		self.details = nouveau_details
		self.save()

	#	apprenants = self.apprenant_domaine.all()
	#	return ", ".join([apprenant.nom for apprenant in apprenants])

