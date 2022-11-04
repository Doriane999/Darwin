from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def liste_contact(request) :
    return HttpResponse("liste contact")

def fiche_contact(request) :
    return HttpResponse("fiche contact")

def creer_contact(request) :
    context = {'first_name' : 'toto', 'last_name' : 'tata'}
    return render(request, "base.html", context)

def modifier_contact(request) :
    return HttpResponse("modifier contact")

def supprimer_contact(request) :
    return HttpResponse("supprimer contact")


