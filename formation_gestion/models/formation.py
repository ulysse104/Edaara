from django.db import models
from .domaine import Domaine

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    createur = models.ForeignKey('user_gestion.Formateur', related_name='formations', on_delete=models.CASCADE)
    domaines = models.ManyToManyField(Domaine, related_name='formations')
    mentors = models.ManyToManyField('user_gestion.Mentor', related_name='formations')

    def __str__(self):
        return f'{self.titre}'


	#def affichage_apprenants_domaine(self)
	#	apprenants = self.apprenant_domaine.all()
	#	return ", ".join([apprenant.nom for apprenant in apprenants])

