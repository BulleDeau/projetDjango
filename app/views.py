# from django.http import HttpResponse
import os
from django.shortcuts import render
from django.http import FileResponse

data_dir = os.path.join(os.path.dirname(__file__), "../docker/data")
images = [f for f in os.listdir(data_dir) if f.endswith(".png")]

def index(request):
    context = {
        "nom" : "tout le monde",
        "images" : images,
        "breadcrumb" : [("Accueil", "/")]
        }
    return render(request, "index.html", context)

def truc_detail(request, nom):
    context = {
        "nom": nom,
        "breadcrumb": [("Accueil", "/"), (nom, f"/truc/{nom}")]
    }
    return render(request, "truc_detail.html", context)

def raw_truc(request, nom):
    # Chemin complet vers ton dossier contenant les images
    data_dir = os.path.join(os.path.dirname(__file__), "../docker/data")
    file_path = os.path.join(data_dir, nom)

    # Vérifie que le fichier existe avant de le renvoyer
    if not os.path.exists(file_path):
        from django.http import Http404
        raise Http404("Fichier non trouvé")

    # Renvoie le contenu brut du fichier image
    return FileResponse(open(file_path, 'rb'), content_type='image/png')