# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "nom" : "tout le monde",
        "breadcrumb" : [("Accueil", "/")]
        }
    return render(request, "index.html", context)