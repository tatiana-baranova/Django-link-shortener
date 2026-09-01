from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Вкажіть Email", 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'})
        )
    username = forms.CharField(
        label="Вкажіть ім'я", 
        required=True, 
        help_text="Обов'язкове поле.Не більше 150 символів. Не використовуйте символи: @, /, _",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"})
        )
    password1 = forms.CharField(
        label="Вкажіть пароль", 
        required=True,
        help_text=mark_safe(
            """ <ul class="password-rules"> <li>Ваш пароль не повинен збігатися з вашим ім'ям або іншою особистою інформацією.</li> <li>Ваш пароль повинен містити не менше 8 символів.</li> <li>Ваш пароль не може бути одним із поширених паролів.</li> <li>Ваш пароль не може складатися лише з цифр.</li> </ul> """),

        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder':'Пароль'})
            )

    class Meta:
        model = User
        fields = ['username', 'email','password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        from django.contrib.auth.password_validation import validate_password
        validate_password(password, self.instance)
        return password


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
            label="Вкажіть Email", 
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'})
            )
    username = forms.CharField(
            label="Вкажіть ім'я", 
            required=True, 
            help_text='Не використовуйте символи: @, /, _',
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"})
            )
    class Meta:
        model = User
        fields = ['username', 'email']
