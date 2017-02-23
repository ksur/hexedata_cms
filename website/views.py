from django.shortcuts import render


# main page
def index(request):
    metaTitle = 'Hexe Data. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'index.html', context)

# page oferta
def oferta(request):
    metaTitle = 'Hexe Data. Oferta. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'oferta.html', context)

# page kompetencje
def kompetencje(request):
    metaTitle = 'Hexe Data. Kompetencje. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'kompetencje.html', context)

# psage kontakt
def kontakt(request):
    metaTitle = 'Hexe Data. Kontakt. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'kontakt.html', context)


