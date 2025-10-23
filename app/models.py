from django.db import models

# faire évoluer le modèle pour que Django gère automatiquement les fichiers (upload, accès, stockage, etc.) au lieu d’un simple texte de chemin.



class MonTruc(models.Model):
    name = models.CharField(max_length=200)
    path = models.FileField(upload_to='', blank=True)  # au lieu de : path = models.CharField(max_length=200)
        # FileField dit à Django : “ce champ correspond à un fichier sur le disque”.
        # L’argument upload_to='' signifie que les fichiers seront directement placés dans MEDIA_ROOT (donc dans app/docker/data/).


# Cette méthode sert à définir la représentation textuelle de l'objet Python 
# c’est-à-dire ce que Django affichera quand il doit “nommer” l'objet (dans l’administration ou dans la console).
def __str__(self):
    return self.name    # transforme 'MonTruc object (1)' en 'MlleA1.png'