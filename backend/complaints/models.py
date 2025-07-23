from django.db import models

from machines.models import ReferenceItem, Machine
from accounts.models import ServiceCompany


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

    failure_date = models.DateField('Дата отказа')
    operating_hours = models.IntegerField('Наработка, м/час')
    failure_node_description = models.TextField('Описание отказа')
    status = models.CharField(choices=STATUS, default='new', verbose_name='Статус')

    failure_node = models.ForeignKey(FailureNode, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Узел отказа')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints', verbose_name='Сервисная компания')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='complaints', verbose_name='Машина')

    # fields that will be added gradually by service company
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Способ восстановления')
    used_spare_parts = models.TextField(null=True, blank=True, verbose_name='Используемые запасные части')
    recovery_date = models.DateField(null=True, blank=True, verbose_name='Дата восстановления')
    downtime = models.CharField(max_length=25, null=True, blank=True, verbose_name='Время простоя техники')

    def __str__(self):
        return f'Рекламация №{self.pk}'
