"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import IndexView, TrucDetailView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),                            # page liste
    path("truc/<int:pk>/", TrucDetailView.as_view(), name="truc_detail"),   # détail
    path('rawtruc/<str:nom>/', views.raw_truc, name='raw_truc'),
] + debug_toolbar_urls()
