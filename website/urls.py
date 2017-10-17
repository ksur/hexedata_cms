from django.conf.urls import url
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kompetencje/', views.kompetencje, name='kompetencje'),
    url(r'kontakt/', views.kontakt, name='kontakt'),
    url(r'oferta/', views.oferta, name='oferta'),
    url(r'onas/', views.onas, name='onas'),
    url(r'index/', views.index),
    url(r'narzedzia/', views.narzedzia, name='narzedzia'),
    url(r'newsroom/', views.newsroom, name='newsroom'),
    url(r'analiza-danych/', views.analizaDanych, name='analizaDanych'),
    url(r'visual-analytics/', views.visualAnalytics, name='visualAnalytics'),
    url(r'wdrozenia-analityczne/', views.wdrozeniaAnalityczne, name='wdrozeniaAnalityczne'),
    url(r'optymalizacja-konwersji/', views.optymalizacjaKonwersji, name='optymalizacjaKonwersji'),
    url(r'^blog/$', RedirectView.as_view(url='http://hexedata.com/blog/index.php'), name='blog'),
]
