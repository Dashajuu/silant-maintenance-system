from django.db import models

from machines.models import ReferenceItem, Machine
from service_company.models import ServiceCompany


class FailureNode(ReferenceItem):
    class Meta:
        verbose_name = 'Узел отказа'


class RecoveryMethod(ReferenceItem):
    class Meta:
        verbose_name = 'Способ восстановления'


class Complaint(models.Model):
    STATUS = [
        ('new', 'Новая'),
        ('under_review', 'На рассмотрении'),
        ('in_progress', 'В процессе ремонта'),
        ('resolved', 'Работы завершены'),
        ('closed', 'Закрыта'),
        ('rejected', 'Отклонена'),
    ]

    failure_date = models.DateField()
    operating_hours = models.IntegerField()
    failure_node_description = models.TextField()
    status = models.CharField(choices=STATUS, default='new')

    failure_node = models.ForeignKey(FailureNode, on_delete=models.SET_NULL, null=True, blank=True)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='complaints')

    # fields that will be added gradually by service company
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.SET_NULL, null=True, blank=True)
    used_spare_parts = models.TextField(null=True, blank=True)
    recovery_date = models.DateField(null=True, blank=True)
    downtime = models.CharField(max_length=25, null=True, blank=True)
