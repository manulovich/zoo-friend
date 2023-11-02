from django.db import models
import uuid
from userprofile.models import UserAccount


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Кличка')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    isOwnerFound = models.BooleanField(default=False)
    kind = models.ForeignKey(
        'Kind', on_delete=models.PROTECT, verbose_name='Вид')
    color = models.ForeignKey(
        'Color', on_delete=models.PROTECT, verbose_name='Цвет')
    age = models.IntegerField(verbose_name='Возраст (месяцев)')
    gender = models.ForeignKey(
        'Gender', on_delete=models.PROTECT, verbose_name='Пол')
    temperament = models.ForeignKey(
        'Temperament', on_delete=models.PROTECT, verbose_name='Темперамент')
    heightAtWithers = models.IntegerField(verbose_name='Высота в холке (см)')
    attitudeTowardsOtherAnimals = models.ForeignKey(
        'AttitudeTowardsOtherAnimals', on_delete=models.PROTECT, verbose_name='Отношение к другим животным')
    specialQualitie = models.ForeignKey(
        'SpecialQualitie', on_delete=models.PROTECT, verbose_name='Особые качества')
    wool = models.ForeignKey(
        'Wool', on_delete=models.PROTECT,  verbose_name='Шерсть')
    owner = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True)
    inFavorites = models.ManyToManyField(UserAccount, related_name='infavorites_animal_set')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль животного'
        verbose_name_plural = 'Профили животных'
        ordering = ['name']


class Kind(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'


class Color(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Окрас животного'
        verbose_name_plural = 'Окрас животных'


class Gender(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Пол животного'
        verbose_name_plural = 'Пол животных'


class Temperament(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Темперамент животного'
        verbose_name_plural = 'Темпераменты животных'


class AttitudeTowardsOtherAnimals(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Отношение к другим животным'
        verbose_name_plural = 'Отношения к другим животным'


class SpecialQualitie(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Особое качество'
        verbose_name_plural = 'Особые качества'


class Wool(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Шерсть животного'
        verbose_name_plural = 'Шерсть животных'
