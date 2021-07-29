from django.db import models

# Create your models here.


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True,
    )
    name = models.TextField(
        verbose_name='Логин пользователя'
    )
    firstname = models.TextField(
        verbose_name='Имя пользователя'
    )

    created_at = models.DateTimeField(
        verbose_name='Время первого запуска',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Время создания:{self.created_at}, ID:{self.external_id}, Логин:{self.name}, ' \
               f'Имя:{self.firstname}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'