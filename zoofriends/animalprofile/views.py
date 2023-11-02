from typing import Any
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import Animal
from .forms import AddAnimalprofileForm
from userprofile.models import UserAccount


def index(request, animal_id):
    animal = Animal.objects.get(id=animal_id)

    if not request.user.is_authenticated:
        user_account = None
        is_in_favorites = False
    else:
        user_account = request.user.useraccount
        is_in_favorites = user_account in animal.inFavorites.all()

    return render(
        request,
        'animalprofile/index.pug',
        {
            'animal': animal,
            'user_account': user_account,
            'is_in_favorites': is_in_favorites
        }
    )


@login_required
def new_animalprofile(request):
    if request.method == 'POST':
        form = AddAnimalprofileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user_id = request.user.useraccount.id
                Animal.objects.create(owner=UserAccount.objects.get(
                    id=user_id), **form.cleaned_data)
                return redirect('/userprofile/')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddAnimalprofileForm()

    return render(request, 'animalprofile/new_animalprofile.pug', {'form': form})


class UpdateAnimal(UpdateView):
    model = Animal
    queryset = Animal.objects.all()
    template_name = 'animalprofile/update_animalprofile.pug'
    pk_url_kwarg = 'pk'
    form_class = AddAnimalprofileForm
    success_url = '/userprofile/'


@login_required
def check_owner_found(request, id):
    animal = Animal.objects.get(id=id)
    animal.isOwnerFound = not animal.isOwnerFound
    animal.save()
    return redirect('/userprofile/')

@login_required
def toggle_in_favorites(request, user_id, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
        user_account = UserAccount.objects.get(id=user_id)

        if user_account in animal.inFavorites.all():
            animal.inFavorites.set(animal.inFavorites.all().exclude(id = user_account.id))
            return HttpResponse('Удалено из избранных')
        else:
            animal.inFavorites.add(user_account)
            return HttpResponse('Добавлено в избранное')
    except:
        return HttpResponse('Серверная ошибка', status=500)