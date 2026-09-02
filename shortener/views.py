from django.shortcuts import render


def home(request):
    return render(request, 'shortener/home.html', {
        'title': 'Головна'
    })

def about(request):
    return render(request, 'shortener/about.html', {'title': 'Про нас'})