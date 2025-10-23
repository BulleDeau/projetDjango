from django import forms
from .models import MonTruc

class MonTrucForm(forms.ModelForm):
    class Meta:
        model = MonTruc                    # le modèle sur lequel le formulaire est basé
        fields = ['name', 'path']          # les champs à inclure dans le formulaire
