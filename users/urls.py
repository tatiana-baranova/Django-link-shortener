from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('', authViews.LoginView.as_view(template_name='users/user.html',extra_context={
            'title': 'Сторінка авторизації'
        }), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html', extra_context={
            'title': 'Сторінка виходу'
        }), name='exit'),
]