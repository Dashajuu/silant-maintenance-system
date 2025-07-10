from django.db import models
from django.core.validators import RegexValidator

from machines.models import ReferenceItem, Machine
from service_company.models import ServiceCompany
from complaints.models import Complaint
from accounts.models import ServiceMaster


class MaintenanceType(ReferenceItem):
    class Meta:
        verbose_name = 'Вид ТО'


class Maintenance(models.Model):
    STATUS = [
        ('new', 'Новая'),
        ('under_review', 'На рассмотрении'),
        ('in_progress', 'В процессе'),
        ('closed', 'ТО проведено'),
        ('complaint', 'Создана рекламация по причине неисправности'),
        ('rejected', 'Отклонена'),
    ]

    work_order_number_validator = RegexValidator(regex=r'^#[A-Za-zА-Яа-я0-9_ №\-.]+$',
                                               message='Номер заказ-наряда должен быть в формате: #2025-32КЕ5СИЛ')

    operating_hours = models.IntegerField(verbose_name='Наработка, м/час')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True, related_name='maintenance',
                                verbose_name='Машина')

    # request fields: blank=True is used in case user wants to submit a request for maintenance
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Вид ТО')
    maintenance_date = models.DateField(null=True, blank=True, verbose_name='Дата проведения ТО')
    work_order_number = models.CharField(validators=[work_order_number_validator], max_length=50, null=True, blank=True, verbose_name='Номер заказ-наряда')
    work_order_date = models.DateField(null=True, blank=True, verbose_name='Дата заказ-наряда')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сервисная компания')
    status = models.CharField(choices=STATUS, null=True, blank=True, verbose_name='Статус')

    # service fields: fields that the service company can fill after receiving a maintenance request from the client
    service_company_respond = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    complaint_number = models.ForeignKey(Complaint, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Номер рекламации')
    service_master = models.ForeignKey(ServiceMaster, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Мастер')
