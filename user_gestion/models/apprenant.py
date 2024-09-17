from django.db import models
from .user import User
from .formateur import Mentor
from formation_gestion.models.domaine import Domaine
from formation_gestion.models.formation import Formation


class Apprenant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='apprenants')
	diplome_eleve = models.CharField(max_length=100, choices=[('bac', 'Baccalaureat'), ('bts', 'BTS'), ('licence', 'Licence'), ('maitrise', 'Maitrise'), ('master', 'Master'), ('doctorat', 'Doctorat')], default='bac')
	domaines_interet = models.ManyToManyField(Domaine, related_name='apprenants')
	formations_suivies = models.ManyToManyField(Formation, related_name='apprenants', blank=True)
	mes_mentors = models.ManyToManyField(Mentor, related_name='apprenants', blank=True)
	REQUIRED_FIELDS = ['user', 'diplome_eleve', 'domaines_interet']
	#mes_certifications = []

	def __str__(self):
		return f'{self.user}'