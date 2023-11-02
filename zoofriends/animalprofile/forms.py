from django import forms
from .models import *


class AddAnimalprofileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Animal
        fields = [
            'name', 'description', 'photo',
            'kind', 'color', 'age', 'gender',
            'temperament', 'heightAtWithers', 'attitudeTowardsOtherAnimals',
            'specialQualitie', 'wool'
        ]
        select_fields = [
            'kind', 'color', 'gender', 'temperament',
            'attitudeTowardsOtherAnimals', 'specialQualitie',
            'wool'
        ]
        widgets = {}

        for field in select_fields:
            widgets[field] = forms.Select()