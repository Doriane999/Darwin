from django.urls import path
from . import views

urlpatterns = [
    path('appli', views.liste_contact, name='liste_contacts'),
    path('fiche', views.fiche_contact, name='fiche_contact'),
    path('creer', views.creer_contact, name='creer_contact'),
    path('modifier', views.modifier_contact, name='modifier_contact '),
    path('supprimer', views.supprimer_contact, name='supprimer_compte'),
    ]