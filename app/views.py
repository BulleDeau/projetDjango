# from django.http import HttpResponse
import os
from django.shortcuts import render
from django.http import FileResponse
from . import models
from django.views.generic import ListView, DetailView


data_dir = os.path.join(os.path.dirname(__file__), "../docker/data")
# images = [f for f in os.listdir(data_dir) if f.endswith(".png")]

# Vue pour la page d’accueil (liste des trucs)
class IndexView(ListView):
    model = models.MonTruc
    template_name = "index.html"          # template
    context_object_name = "trucs"         # nom utilisé dans le template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        # Récupère le contexte de base généré par ListView
        context["titre"] = "Liste des trucs disponibles"    # infos supplémentaires :
        return context

# Vue pour le détail d’un truc
class TrucDetailView(DetailView):
    model = models.MonTruc
    template_name = "truc_detail.html"      # template
    context_object_name = "truc"            # nom utilisé dans le template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = [
            ("Accueil", "/"),
            (self.object.name, f"/truc/{self.object.pk}/")
        ]
        return context


# def index(request):
#     trucs = models.MonTruc.objects.all()  
#     context = {
#         "nom" : "tout le monde",
#         "images" : trucs,
#         "breadcrumb" : [("Accueil", "/")]
#         }
#     return render(request, "index.html", context)

# def truc_detail(request, nom):
#     context = {
#         "nom": nom,
#         "breadcrumb": [("Accueil", "/"), (nom, f"/truc/{nom}")]
#     }
#     return render(request, "truc_detail.html", context)

def raw_truc(request, nom):
    # Chemin complet vers ton dossier contenant les images
    data_dir = os.path.join(os.path.dirname(__file__), "../docker/data")
    file_path = os.path.join(data_dir, nom)
    # Vérifie que le fichier existe avant de le renvoyer
    if not os.path.exists(file_path):
        from django.http import Http404
        raise Http404("objet non trouvé")

    # Renvoie le contenu brut du fichier image
    return FileResponse(open(file_path, 'rb'), content_type='image/png')

