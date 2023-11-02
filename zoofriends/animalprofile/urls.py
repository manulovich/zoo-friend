from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('new/', new_animalprofile),
    path('edit/<uuid:pk>/', UpdateAnimal.as_view()),
    path('check-owner-found/<uuid:id>/', check_owner_found),
    path('toggle-in-favorites/<uuid:user_id>/<uuid:animal_id>', toggle_in_favorites),
]