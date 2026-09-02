from django import forms
from .models import Link

class LinkShortenerForm(forms.Form):
    original_url = forms.URLField(
        label = 'Оригінальне посилання:',
        max_length=250,
        help_text='Переконайтеся, що це значення містить не більше 250 символів.',
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Введіть оригінальне посилання',
            }
        ),
        error_messages={
        'required': 'Будь ласка, вкажіть оригінальне посилання.',
        'invalid': 'Введіть коректну URL-адресу.',
        }
    )

    short_url = forms.CharField(
        label = 'Скорочене посилання:',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'some',
            }
        ),
        error_messages={
            'required': 'Будь ласка, вкажіть скорочене посилання.',
        }
    )

    def clean_short_url(self):
        short_url = self.cleaned_data.get('short_url')

        if Link.objects.filter(short_url=short_url).exists():
            raise forms.ValidationError(
                'Посилання з таким скороченим кодом вже існує.'
            )

        return short_url
