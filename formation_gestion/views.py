#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
#from rest_framework.response import response
from formation_gestion.serializers import FormationSerializer, DomaineSerializer
from formation_gestion.models import Formation, Domaine

# Create your views here.

class FormationViewSet(ModelViewSet):

	serializer_class = FormationSerializer

	def get_queryset(self):
		return Formation.objects.all()


class DomaineViewSet(ReadOnlyModelViewSet):
	serializer_class = DomaineSerializer

	def get_queryset(self):
		return Domaine.objects.all()