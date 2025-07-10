from django.db import models
from django.core.validators import RegexValidator

from accounts.models import Client
from service_company.models import ServiceCompany


class ReferenceItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MachineType(ReferenceItem):
    class Meta:
        verbose_name = 'Модель техники'


class EngineType(ReferenceItem):
    class Meta:
        verbose_name = 'Модель двигателя'


class TransmissionType(ReferenceItem):
    class Meta:
        verbose_name = 'Модель трансмиссии'


class DriveAxleType(ReferenceItem):
    class Meta:
        verbose_name = 'Модель ведущего моста'


class SteerAxleType(ReferenceItem):
    class Meta:
        verbose_name = 'Модель управляемого моста'


class Machine(models.Model):
    supply_contract_validator = RegexValidator(regex=r'^[A-Za-zА-Яа-я0-9_ №\-.]+$',
                                               message='Номер и дата договора должны быть в формате (разрешены буквы, цифры, дефис): №9999-999 01.01.2025')

    supply_contract_number_date = models.CharField(validators=[supply_contract_validator], max_length=150)
    shipment_date = models.DateField()
    consignee_end_customer = models.CharField(max_length=150)
    operating_address = models.CharField(max_length=150)
    equipment = models.TextField(default='Стандарт')

    # unique fields
    machine_serial_number = models.CharField(max_length=50, unique=True)
    engine_serial_number = models.CharField(max_length=50, unique=True)
    transmission_serial_number = models.CharField(max_length=50, unique=True)
    drive_axle_serial_number = models.CharField(max_length=50, unique=True)
    steer_axle_serial_number = models.CharField(max_length=50, unique=True)

    # foreign key relation
    machine_type = models.ForeignKey(MachineType, on_delete=models.SET_NULL, null=True, blank=True)
    engine_type = models.ForeignKey(EngineType, on_delete=models.SET_NULL, null=True, blank=True)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.SET_NULL, null=True, blank=True)
    drive_axle_type = models.ForeignKey(DriveAxleType, on_delete=models.SET_NULL, null=True, blank=True)
    steer_axle_type = models.ForeignKey(SteerAxleType, on_delete=models.SET_NULL, null=True, blank=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='machines')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.SET_NULL, null=True, blank=True, related_name='machines')


