from django.shortcuts import redirect, render
from animalprofile.models import Animal, Kind
from userprofile.models import UserAccount
from .forms import SearchAnimalsForm

def index(request):
    if request.method == 'POST':
        form = SearchAnimalsForm(request.POST)
        if form.is_valid():
            try:            
                params_search = dict()
                req_post = request.POST.dict()

                for field, value in form.cleaned_data.items():
                    if field == 'age': continue
                    if str(value) == 'не указано': continue
                    
                    params_search[field] = req_post[field]

                params_search['age__lte'] = int(req_post['age'])
                params_search['isOwnerFound'] = False

                animals = Animal.objects.filter(**params_search)
            except:
                form.add_error(None, 'Ошибка поиска')
    else:
        form = SearchAnimalsForm()
        animals = Animal.objects.filter(isOwnerFound=False)

    count_animals = len(animals)
    user = request.user

    if user.is_authenticated:
        user_account = user.useraccount
        animal_list = list()

        for animal in animals:
            animal_list.append({
                'id': animal.id,
                'name': animal.name,
                'photo': animal.photo,
                'isOwnerFound': animal.isOwnerFound,
                'isFavorite': user_account in animal.inFavorites.all()
            })
    else:
        user_account = None
        animal_list = animals

    return render(
        request,
        'animalprofiles/index.pug',
        {
            'animals': animal_list,
            'user_account': user_account,
            'count_animals': count_animals,
            'form': form
        }
    )
