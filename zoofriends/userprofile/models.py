from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Contact(models.Model):
    email = models.EmailField(blank=True, verbose_name='Электронная почта')
    tel = PhoneNumberField(region='RU', blank=True)
    vk = models.URLField(blank=True, verbose_name='ВКонтакте')
    tg = models.URLField(blank=True, verbose_name='Телеграм')

    def __str__(self):
        return f'email-{self.email}  tel-{self.tel}  vk-{self.vk}  tg-{self.tg}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner_shelter = models.BooleanField(
        default=False, verbose_name='Представитель приюта?')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    preferences = models.CharField(
        max_length=255, verbose_name='Предпочтения', blank=True)
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
