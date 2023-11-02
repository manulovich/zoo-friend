from django import forms
from animalprofile.models import *

# https://stackoverflow.com/questions/1336900/django-modelchoicefield-and-initial-value


class SearchAnimalsForm(forms.Form):
    kind = forms.ModelChoiceField(
        queryset=Kind.objects.all(),
        label='Вид',
        empty_label=None,
        initial=Kind.objects.get(id=1)
    )
    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        label='Цвет',
        empty_label=None,
        initial=Color.objects.get(id=1)
    )
    age = forms.IntegerField(
        label='Возраст до (месяцев)',
        initial=100
    )
    gender = forms.ModelChoiceField(
        queryset=Gender.objects.all(),
        label='Пол',
        empty_label=None,
        initial=Gender.objects.get(id=1)
    )
    temperament = forms.ModelChoiceField(
        queryset=Temperament.objects.all(),
        label='Темперамент',
        empty_label=None,
        initial=Temperament.objects.get(id=1)
    )
    attitudeTowardsOtherAnimals = forms.ModelChoiceField(
        queryset=AttitudeTowardsOtherAnimals.objects.all(),
        label='Отношение к другим животным',
        empty_label=None,
        initial=AttitudeTowardsOtherAnimals.objects.get(id=1)
    )
    specialQualitie = forms.ModelChoiceField(
        queryset=SpecialQualitie.objects.all(),
        label='Особые качества',
        empty_label=None,
        initial=SpecialQualitie.objects.get(id=4)
    )
    wool = forms.ModelChoiceField(
        queryset=Wool.objects.all(),
        label='Шерсть',
        empty_label=None,
        initial=Wool.objects.get(id=3)
    )
