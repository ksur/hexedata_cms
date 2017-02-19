from django.shortcuts import render


# Create your views here.
def index(request):
    metaTitle = 'Hexe Data. Analityka Internetowa'
    context = {
        'metaTitle' : metaTitle,
    }
    return render(request, 'index.html', context)


def oferta(request):
    return render(request, 'oferta.html')


def kompetencje(request):
    return render(request, 'kompetencje.html')


def kontakt(request):
    return render(request, 'kontakt.html')


