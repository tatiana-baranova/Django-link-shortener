from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Користувач {username} успішно зареєстрований')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/registration.html', {'title': 'Сторінка реєстрації', 'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        update_user_form = UserUpdateForm(request.POST, instance=request.user)

        if update_user_form.is_valid():
            update_user_form.save()

            messages.success(request, "Профіль успішно оновлений")
            return redirect('profile')
    else:
        update_user_form = UserUpdateForm(instance=request.user)


    data = {
        'update_user_form': update_user_form
    }
    return render(request, 'users/profile.html', data)