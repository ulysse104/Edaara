from rest_framework.serializers import ModelSerializer
from formation_gestion.models import Formation, Domaine

class FormationSerializer(ModelSerializer):

	class Meta :
		model = Formation
		fields = ['titre', 'domaines']


class DomaineSerializer(ModelSerializer):

	class Meta :
		model = Domaine
		fields = ['domaine']