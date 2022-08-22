from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.shortcuts import get_object_or_404
from app.forms import ProductionForm
# Create your views here..

class HomePageView(TemplateView):
    template_name = "app/home.html"



# fenetre etapes crud
class EtapPageView(ListView):
    template_name = "app/etapeProd.html"
    model = etape
    
class EtapeDetailView(DetailView):
    model = etape
    template_name = "app/DetailEtape.html"
# fin fentre etape


# fenetre production crud
class ProduitPageView(ListView):
    template_name = "app/production.html"
    model = production


class ProduitDetailView(DetailView):
    template_name = "app/DetailProduction.html"
    model = production

    
class ProductionCreateView(CreateView):
    template_name = "app/AjoutProduction.html"
    model = production
    form_class = ProductionForm


class ProductionEditeView(UpdateView):
    model = production
    template_name = "app/AjoutProduction.html"
    form_class = ProductionForm
    
# fin de la fenetre production  


# crud fenetre client
class ClientPageView(ListView):
    template_name = "app/client.html"
    model = client






# fin fenetre client


# crud fenetre fournisseur
class FournisseurPageView(ListView):
    template_name = "app/fournisseur.html"
    model = fournisseur
