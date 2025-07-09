from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import Manager, Client, ServiceMaster, ContactPerson
from service_company.models import ServiceCompany


# validators
phone_regex = RegexValidator(regex=r'^\+7\d{10}$',
                             message="Номер должен быть в формате: '+79123456789' (11 цифр с кодом страны)"
                             )

telegram_validator = RegexValidator(regex=r'^@[A-Za-zА-Яа-я0-9_]+$',
                                    message='Ник должен начинаться с @ и содержать только буквы, цифры и _'
                                    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    phone_number = forms.CharField(max_length=17, required=False, label='Телефон', validators=[phone_regex])
    email = forms.EmailField(label='Email', required=False)
    telegram = forms.CharField(required=False, label='Telegram', validators=[telegram_validator])

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
            Manager.objects.get_or_create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                telegram=self.cleaned_data['telegram'],
                region=self.cleaned_data['region'],
            )
        return user


class ClientCreationForm(CustomUserCreationForm):
    name = forms.CharField(max_length=150, label='Название компании')

    class Meta(CustomUserCreationForm.Meta):
        fields = CustomUserCreationForm.Meta.fields + ('name',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        manager = Manager.objects.get(id=1) #TODO: possibility to choose manager by user

        if commit:
            Client.objects.get_or_create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                telegram=self.cleaned_data['telegram'],
                manager=manager,
            )
        return user


class ServiceMasterCreationForm(CustomUserCreationForm):
    position = forms.CharField(max_length=150, label='Должность')
    service_company = forms.ModelChoiceField(queryset=ServiceCompany.objects.all(), label='Сервисная компания')

    class Meta(CustomUserCreationForm.Meta):
        fields = CustomUserCreationForm.Meta.fields + ('position',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        service_company = self.cleaned_data['service_company']

        if commit:
            ServiceMaster.objects.get_or_create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                telegram=self.cleaned_data['telegram'],
                service_company = service_company,
            )
        return user


class ContactPersonCreationForm(CustomUserCreationForm):
    service_company = forms.ModelChoiceField(queryset=ServiceCompany.objects.all(), label='Сервисная компания')

    class Meta(CustomUserCreationForm.Meta):
        fields = CustomUserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super().save(commit=commit)
        service_company = self.cleaned_data['service_company']

        if commit:
            ContactPerson.objects.get_or_create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                telegram=self.cleaned_data['telegram'],
                service_company=service_company,
            )
        return user
