# Introduction a Django, &emsp;David Beniamine, &emsp;Handigital, 08/10/25

## Description

## Sommaire
- [Ajouter bootstrap](#ajouter-bootstrap)
- [Template et héritage](#template-et-héritage)


## Ajouter bootstrap
Ajouter dans votre image (Dockerfile) le paquet pip django-bootstrap5  
Ajouter dans les INSTALLED_APPS (settings.py): django_bootstrap5  
Dans le head de votre template (index.html) ajouter : 
&emsp;{% load django_bootstrap5 %}  
&emsp;{% bootstrap_css %}  
&emsp;{% bootstrap_javascript %}  
Vous pouvez désormais mettre des classes bootstrap  
Pour aller plus loin: https://django-bootstrap-v5.readthedocs.io/en/latest

## Template et héritage
créer une structure de templates Django réutilisable (avec un layout de base, un héritage de templates, et un fil d’Ariane — breadcrumb).  
1) Ajouter un dossier template  
&emsp;app/templates/layouts/base.html  

2) base.html contient une structure html de base avec un <body> et l’instruction {% block content %}{% endblock %}  
Ce fichier contient la structure HTML commune (entête, pied de page, CSS/JS, etc.)  
et une zone modifiable appelée block content.  
3) Hérite de base  
4) Ajouter un fil d’ariange breadcrumb dans le layout  

