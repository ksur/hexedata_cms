from django.shortcuts import render


# main page
def index(request):
    metaTitle = 'Hexe Data. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'index.html', context)

# page oferta ##############################################
def oferta(request):
    metaTitle = 'Hexe Data. Oferta. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'oferta.html', context)

def analizaDanych(request):
    return render(request, 'oferta/analiza_danych.html')

def visualAnalytics(request):
    return render(request, 'oferta/visual_analytics.html')

def wdrozeniaAnalityczne(request):
    return render(request, 'oferta/wdrozenia_analityczne.html')

def optymalizacjaKonwersji(request):
    return render(request, 'oferta/optymalizacja_konwersji.html')

# end page oferta ##############################################

# page kompetencje
def kompetencje(request):
    metaTitle = 'Hexe Data. Kompetencje. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'kompetencje.html', context)

# page kontakt
def kontakt(request):
    metaTitle = 'Hexe Data. Kontakt. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'kontakt.html', context)

# page narzedzia
def narzedzia(request):
    metaTitle = 'Hexe Data. Kontakt. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'kontakt.html', context)

# page newsroom
def newsroom(request):
    metaTitle = 'Hexe Data. Kontakt. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'newsroom.html', context)

# page onas
def onas(request):
    metaTitle = 'Hexe Data. O nas'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'onas.html', context)