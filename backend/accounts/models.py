from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from service_company.models import ServiceCompany


class BaseModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+7\d{10}$',
                                 message="Номер должен быть в формате: '+79123456789' (11 цифр с кодом страны)")
    telegram_validator = RegexValidator(
        regex=r'^@[A-Za-zА-Яа-я0-9_]+$',
        message='Ник должен начинаться с @ и содержать только буквы, цифры и _'
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(validators=[telegram_validator], max_length=32, blank=True, null=True)

    class Meta:
            abstract = True


class ServiceMaster(BaseModel):
    position = models.CharField('Должность', max_length=150, blank=True, null=True)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, related_name='service_master', verbose_name='Сервисная компания')


# Service company's contact person: just for case
class ContactPerson(BaseModel):
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, related_name='contact_person')


class Manager(BaseModel):
    region = models.CharField('Регион', max_length=150, blank=True, null=True)

# Zero manager for saving clients in case deleting a real manager
def get_fault_manger():
    return 1


class Client(BaseModel):
    name = models.CharField('Название компании', max_length=150)
    manager = models.ForeignKey(Manager,on_delete=models.SET_DEFAULT, default=get_fault_manger, related_name='clients')

    def __str__(self):
        return self.name