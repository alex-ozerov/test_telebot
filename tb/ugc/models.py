from django.db import models

# Create your models here.


class Profile(models.Model):
    user_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True,
    )
    username = models.TextField(
        verbose_name='Логин пользователя'
    )
    firstname = models.TextField(
        verbose_name='Имя пользователя'
    )
    lastname = models.TextField(
        verbose_name='Фамилия пользователя'
    )
    created_at = models.DateTimeField(
        verbose_name='Время первого запуска',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Время создания:{self.created_at}, ID:{self.user_id}, Логин:{self.username}, ' \
               f'Имя:{self.firstname}, Фамилия:{self.lastname}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
