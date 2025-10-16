# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    nom = "Toto"
    return render(request, "index.html", {"nom": nom})