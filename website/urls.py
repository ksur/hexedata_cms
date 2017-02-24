from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^kompetencje/', views.kompetencje),
    url(r'kontakt/', views.kontakt),
    url(r'oferta/', views.oferta),
    url(r'onas/', views.oferta),
    url(r'index/', views.index),
    url(r'narzedzia/', views.narzedzia),
    url(r'newsroom/', views.newsroom),
]
