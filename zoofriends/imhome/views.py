from django.shortcuts import render
from animalprofile.models import Animal


def index(request):
    animals = Animal.objects.filter(isOwnerFound=True)

    return render(request, 'imhome/index.pug', {'animals': animals})
