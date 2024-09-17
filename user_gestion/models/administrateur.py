from .user import User
from django.db import models

class Administrateur(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrateurs')

	def __str__(self):
		return f'{self.user}'

	