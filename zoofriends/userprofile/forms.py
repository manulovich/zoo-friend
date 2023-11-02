from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm


from .models import UserAccount


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        if User.objects.filter(email=cleaned_data['email']).count() > 0:
            print(self.fields)
            self.add_error('email', 'Почта уже используется')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CreateUserAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserAccount
        fields = ['is_owner_shelter', 'photo']


class SetContactUserForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class LoginUserAccountForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
