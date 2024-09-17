#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
#from rest_framework.response import Response
from user_gestion.models import User, Apprenant, Administrateur, Formateur, Mentor
from user_gestion.serializers import UserSerializer, AdministrateurSerializer, ApprenantSerializer, FormateurSerializer, MentorSerializer

# Create your views here.

class UserViewSet(ReadOnlyModelViewSet):

	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.all()


class AdministrateurViewSet(ReadOnlyModelViewSet):

	serializer_class = AdministrateurSerializer

	def get_queryset(self):
		return Administrateur.objects.all()


class ApprenantViewSet(ReadOnlyModelViewSet):

	serializer_class = ApprenantSerializer

	def get_queryset(self):
		return Apprenant.objects.all()

class FormateurViewSet(ReadOnlyModelViewSet):

	serializer_class = FormateurSerializer

	def get_queryset(self):
		return Formateur.objects.all()


class MentorViewSet(ReadOnlyModelViewSet):

	serializer_class = MentorSerializer

	def get_queryset(self):
		return Mentor.objects.all()