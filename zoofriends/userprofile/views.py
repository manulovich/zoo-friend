from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from userprofile.models import UserAccount
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth import login
from animalprofile.models import Animal
from .models import *
from .forms import *


@login_required
def index(request):
    user = request.user
    user_id = user.useraccount.id
    user_account = user.useraccount
    animals = Animal.objects.filter(owner__id=user_id)
    animal_list = list()

    for animal in animals:
        animal_list.append({
            'id': animal.id,
            'name': animal.name,
            'photo': animal.photo,
            'isOwnerFound': animal.isOwnerFound,
            'isFavorite': user_account in animal.inFavorites.all()
        })

    return render(
        request,
        'userprofile/index.pug',
        {
            'user': user,
            'user_account': user_account,
            'animals': animal_list
        }
    )


class CreateUser(CreateView):
    form_class = CreateUserForm
    template_name = 'userprofile/register_user.pug'

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('/userprofile/create-profile/')

        return render(request, 'userprofile/register_user.pug', {'form': form})


class UpdateUserLoginEmail(UpdateView):
    form_class = UpdateUserForm
    template_name = 'userprofile/update_login_email.pug'
    success_url = '/userprofile/'

    def get_object(self):
        return self.request.user


class UpdateUserPassword(PasswordChangeView):
    form_class = SetPasswordForm
    template_name = 'userprofile/update_password.pug'
    success_url = '/userprofile/'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)


class CreateProfile(CreateView):
    form_class = CreateUserAccountForm
    template_name = 'userprofile/create_profile.pug'

    def post(self, request):
        form = CreateUserAccountForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            UserAccount.objects.create(**form.cleaned_data, user=user)
            return redirect('/userprofile/set-contact/')

        return render(request, 'userprofile/create_profile.pug', {'form': form})


class SetContact(CreateView):
    form_class = SetContactUserForm
    template_name = 'userprofile/set_contacts.pug'

    def post(self, request):
        form = SetContactUserForm(request.POST)
        if form.is_valid():
            useraccount = request.user.useraccount

            contact = Contact.objects.create(**form.cleaned_data)
            useraccount.contact = contact
            useraccount.save()

            return redirect('/')

        return render(request, 'userprofile/set_contacts.pug', {'form': form})


class UpdateProfile(UpdateView):
    form_class = CreateUserAccountForm
    template_name = 'userprofile/update_profile.pug'
    success_url = '/userprofile/'

    def get_object(self):
        return self.request.user.useraccount


class LoginUser(LoginView):
    form_class = LoginUserAccountForm
    template_name = 'userprofile/login_user.pug'

    def get_success_url(self):
        return '/userprofile/'


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

# Reset password


class UserForgotPassword(SuccessMessageMixin, PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'userprofile/user_password_reset.pug'
    success_url = '/'
    subject_template_name = 'userprofile/email/password_subject_reset_mail.txt'
    email_template_name = 'userprofile/email/password_reset_mail.html'
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'userprofile/user_password_set_new.pug'
    success_url = '/'
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'
