from django.contrib import admin
from .models import Domaine, Formation, ModuleFormation, Chapitre, Cours, Lien

# Register your models here.



#class DomaineAdmin(admin.ModelAdmin):
   # list_display = ('domaine', 'affichage_apprenants_domaine')

   # def affichage_apprenants_domaine(self, obj):
    #    apprenants = obj.apprenant_domaine.all()
    #    return ", ".join([apprenant.nom for apprenant in apprenants])  # Affiche les noms des apprenants

   # affichage_apprenants_domaine.short_description = 'Apprenants intéressés'

admin.site.register(Domaine)
admin.site.register(Formation)
admin.site.register(ModuleFormation)
admin.site.register(Chapitre)
admin.site.register(Cours)
admin.site.register(Lien)