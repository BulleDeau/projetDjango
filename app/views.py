# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    nom = "tout le monde"
    return render(request, "index.html", {"nom": nom})