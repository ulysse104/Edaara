from django.db import models
from .chapitre import Chapitre

class Lien(Chapitre):
	le_lien = models.URLField()
	

	def __str__(self):
		return f'{self.titre}'

	

