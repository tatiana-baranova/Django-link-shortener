from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Користувач', on_delete=models.CASCADE)
    gender = models.CharField(
        verbose_name='Стать',
        max_length=20,
        choices=[
            ('male', 'Чоловіча'),
            ('female', 'Жіноча'),
        ],
        default='male'
    )
    email_notifications = models.BooleanField(
        verbose_name='Отримання повідомлень на пошту',
        default=False
    )

    def __str__(self):
        return f'Профіль користувача {self.user.username}'

    def save(self, *args, **kwargs):
        if self.pk:
            old = Profile.objects.get(pk=self.pk)


    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'