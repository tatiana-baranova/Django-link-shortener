from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about
from links import views as link_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('users/', include('users.urls')),
    path('links/', include('links.urls')),
    path('link/<str:short_url>/', link_views.redirect_link, name='redirect_link'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
