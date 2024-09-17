from rest_framework.serializers import ModelSerializer
from user_gestion.models import User, Apprenant, Formateur, Mentor, Administrateur
#from formation_gestion.serializers import FormationSerializer

class UserSerializer(ModelSerializer):

	class Meta :
		model = User
		fields = ['nom', 'prenom', 'email']

class AdministrateurSerializer(ModelSerializer):

	class Meta :
		model = Administrateur
		fields = ['user']


class ApprenantSerializer(ModelSerializer):

	user = UserSerializer(read_only=True)

	class Meta :
		model = Apprenant
		fields = ['user', 'domaines_interet', 'formations_suivies']

class FormateurSerializer(ModelSerializer):

	user = UserSerializer(read_only=True)

	class Meta :
		model = Formateur
		fields = ['user', 'profession', 'domaines_expertise']


class MentorSerializer(ModelSerializer):

	formateur = FormateurSerializer(read_only=True)


	class Meta :
		model = Mentor
		fields = ['formateur', '']