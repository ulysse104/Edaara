"""
URL configuration for Edaara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user_gestion.views import UserViewSet, AdministrateurViewSet, ApprenantViewSet, FormateurViewSet, MentorViewSet
from formation_gestion.views import FormationViewSet, DomaineViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('admins', AdministrateurViewSet, basename='admins')
router.register('apprenants', ApprenantViewSet, basename='apprenants')
router.register('formateurs', FormateurViewSet, basename='formateurs')
router.register('mentors', MentorViewSet, basename='mentors')
router.register('formations', FormationViewSet, basename='formations')
router.register('domaines', DomaineViewSet, basename='domaines')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/', include(router.urls)),
]