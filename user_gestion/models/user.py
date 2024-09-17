from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
import datetime
#from django.utils import timezone



class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    
   

class User(AbstractBaseUser):
    nom = models.CharField( max_length=50)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=20, choices=[('feminin', 'Feminin'), ('masculin', 'Masculin')], default='masculin')
    date_naissance = models.DateField(default=datetime.date.today)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)


    groups = models.ManyToManyField(
            Group,
            related_name="users",
            blank=True,
            help_text=("The groups this user belongs to. A user will get all permissions "
                       "granted to each of their groups."),
            related_query_name="user",
        )
        
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_set",
        blank=True,
        help_text=("Specific permissions for this user."),
        related_query_name="user",
    )
    
   # statut = models.CharField(max_length=20, choices=[('apprenant', 'Apprenant'), ('formateur', 'Formateur')], default='apprenant')

    objects = MyUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['nom', 'prenom']

    def __str__(self):
        return f'{self.email}'
    
    

    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

