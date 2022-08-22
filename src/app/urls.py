from app.views import HomePageView, EtapPageView, ProduitPageView, EtapeDetailView, FournisseurPageView, ProductionCreateView, ClientPageView
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name="HomeVue"),
    path('Etape', EtapPageView.as_view(), name="etapeView"),
    path('Production', ProduitPageView.as_view(), name="ProduitView"),
    path('Client', ClientPageView.as_view(), name="ClientView"),
    path('fournisseur', FournisseurPageView.as_view(), name="FournisseurView"),
    path('aboutEtape', EtapeDetailView.as_view(), name="aboutEtape"),
    path('Newproduction/create/', ProductionCreateView.as_view(), name="ProductionAddNew"),
]