from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LinkShortenerForm
from .models import Link


@login_required
def links(request):
    if request.method == 'POST':
        form = LinkShortenerForm(request.POST)

        if form.is_valid():
            Link.objects.create(
                user=request.user,
                original_url=form.cleaned_data['original_url'],
                short_url=form.cleaned_data['short_url']
            )
            return redirect('links')
    else:
        form = LinkShortenerForm()

    user_links = Link.objects.filter(user=request.user)

    return render(
        request,
        'links/links.html',
        {
            'title': 'Мої посилання',
            'form': form,
            'user_links': user_links
        }
    )


def redirect_link(request, short_url):
    try:
        link = Link.objects.get(short_url=short_url)
    except Link.DoesNotExist:
        return render(
            request, 
            'links/link_not_found.html', 
            {'title': 'Посилання не знайдено'}
            )

    return redirect(link.original_url)
