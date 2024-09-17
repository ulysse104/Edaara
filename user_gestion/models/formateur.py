from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .user import User
from formation_gestion.models.domaine import Domaine

class Formateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='formateurs')
    profession = models.CharField(max_length=100)
    domaines_expertise = models.ManyToManyField(Domaine, related_name='formateurs')
    annee_experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(35)], default=0)
    biographie = models.TextField()
    annee_de_mentorat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(35)], default=0)
    disponibilite = models.BooleanField(default=False)
    donnees_banquaire = models.CharField(max_length=200)
    #REQUIRED_FIELDS = ['user', 'profession', 'domaines_expertise', 'annee_experience', 'biographie', 'annee_de_mentorat', 'disponibilite', 'donnees_banquaire']

    def __str__(self):
        return f'{self.user}'

    def est_eligible_pour_mentor(self):
        return self.annee_experience >= 5 and self.annee_de_mentorat >= 3 and self.disponibilite

class Mentor(models.Model):
    formateur = models.OneToOneField(Formateur, on_delete=models.CASCADE, related_name='mentor')

    def __str__(self):
        return f'Mentor: {self.formateur.user}'

    @classmethod
    def creer_mentor(cls, formateur):
        """
        Crée un mentor à partir d'un formateur si celui-ci répond aux critères.
        """
        if formateur.est_eligible_pour_mentor():
            mentor, created = cls.objects.get_or_create(formateur=formateur)
            return mentor
        return None
