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


# Create form
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
                name=self.cleaned_data['name'],
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
                service_company=service_company,
                position=self.cleaned_data['position'],
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



# factory function that generates a form class for custom update account forms
def make_custom_update_form(model_class, *form_fields):
    class CustomUserUpdateForm(forms.ModelForm):
        username = forms.CharField(max_length=150, label='Логин')
        first_name = forms.CharField(max_length=150, required=False, label='Имя')
        last_name = forms.CharField(max_length=150, required=False, label='Фамилия')
        email = forms.EmailField(required=False, label='Email')
        phone_number = forms.CharField(max_length=17, required=False, label='Телефон')
        telegram = forms.CharField(required=False, label='Telegram')

        class Meta:
            model = model_class
            fields = [*form_fields]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance and self.instance.user:
                user = self.instance.user
                self.fields['username'].initial = user.username
                self.fields['first_name'].initial = user.first_name
                self.fields['last_name'].initial = user.last_name
                self.fields['email'].initial = user.email
                self.fields['phone_number'].initial = self.instance.phone_number
                self.fields['telegram'].initial = self.instance.telegram

        def save(self, commit=True):
            account = super().save(commit=False)
            user = account.user
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            account.phone_number = self.cleaned_data['phone_number']
            account.telegram = self.cleaned_data['telegram']

            if commit:
                user.save()
                account.save()
            return account
    return CustomUserUpdateForm