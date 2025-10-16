# Introduction a Django, David Beniamine, Handigital, 08/10/25

## Description

## Sommaire
- [Ajouter bootstrap](#ajouter-bootstrap)
- [Template et héritage](#template-et-héritage)


## Ajouter bootstrap
Ajouter dans votre image le paquet pip django-bootstrap5  
Ajouter dans les INSTALLED_APPS : django_bootstrap5  
Dans le head de votre template ajouter  
&emsp;{% load django_bootstrap5 %}  
&emsp;{% bootstrap_css %}  
&emsp;{% bootstrap_javascript %}  
Vous pouvez désormais mettre des classes bootstrap  
Pour aller plus loin: https://django-bootstrap-v5.readthedocs.io/en/latest

## Template et héritage