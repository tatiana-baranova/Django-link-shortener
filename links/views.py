from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def links(request):
    return render(
        request,
        'links/links.html',
        {
            'title': 'Мої посилання'
        }
    )
