from django.db import models
from django.core.validators import RegexValidator

from machines.models import ReferenceItem
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

    operating_hours = models.IntegerField()

    # blank=True is used in case user wants to submit a request for maintenance
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.SET_NULL, null=True, blank=True)
    maintenance_date = models.DateField(null=True, blank=True)
    work_order_number = models.CharField(validators=[work_order_number_validator], max_length=50, null=True, blank=True)
    work_order_date = models.DateField(null=True, blank=True)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.SET_NULL, null=True, blank=True)

    # fields that the service company can fill after receiving a maintenance request from the client
    status = models.CharField(choices=STATUS, null=True, blank=True)
    service_company_respond = models.TextField(null=True, blank=True)
    complaint_number = models.ForeignKey(Complaint, on_delete=models.SET_NULL, null=True, blank=True)
    service_master = models.ForeignKey(ServiceMaster, on_delete=models.SET_NULL, null=True, blank=True)
