from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Manager


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    phone_number = forms.CharField(max_length=17, required=False, label='Телефон')
    email = forms.EmailField(label='Email', required=False)
    telegram = forms.CharField(required=False, label='Telegram')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name',
                  'phone_number', 'email', 'telegram')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class ManagerCreationForm(CustomUserCreationForm):
    region = forms.CharField(max_length=150, required=False, label='Регион')

    class Meta(CustomUserCreationForm.Meta):
        fields = CustomUserCreationForm.Meta.fields + ('region',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            Manager.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                telegram=self.cleaned_data['telegram'],
                region=self.cleaned_data['region'],
            )
        return user

