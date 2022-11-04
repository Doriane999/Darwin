from django.http import HttpResponse

def index(request):
    return HttpResponse("toto")

def article_annee_mois(request, annee, mois):
    return HttpResponse(f"{annee} {mois}")

def liste_contact(request) :
    return HttpResponse