from django.contrib import admin
from .models import Administrateur, Apprenant, Formateur, Mentor, User #, Domaine

# Register your models here.


class AdministrateurAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
	list_display = ('user',)

class ApprenantAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
	list_display = ('user',)
	list_filter = ('user',)
	search_field = ('user',)

class FormateurAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
	list_display = ('user', 'profession',)
	list_filter = ('user',)
	search_field = ('user',)

class MentorAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
	list_display = ('formateur',)

class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
	list_display = ('nom', 'prenom', 'email')
	list_filter = ('nom', 'email')
	search_field = ('nom', 'email')


admin.site.register(Administrateur, AdministrateurAdmin)
admin.site.register(Apprenant, ApprenantAdmin)
admin.site.register(Formateur, FormateurAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(User, UserAdmin)
