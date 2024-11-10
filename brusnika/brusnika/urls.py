"""
URL configuration for brusnika project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from brapp.views import infoobshee, nametov, registration_page

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration_page),
    path('infoobshee/', infoobshee),
    path('nametov/', nametov),
    path('carzina/', TemplateView.as_view(template_name='carzina.html')),
    path('lenm/', TemplateView.as_view(template_name='katalog tov/lenm.html')),
    path('cmolka/', TemplateView.as_view(template_name='katalog tov/cmolka.html')),
    path('chai/', TemplateView.as_view(template_name='katalog tov/chai.html')),
    path('vodaprop/', TemplateView.as_view(template_name='katalog tov/vodaprop.html')),
    path('bronxo/', TemplateView.as_view(template_name='katalog tov/bronxo.html')),
]

