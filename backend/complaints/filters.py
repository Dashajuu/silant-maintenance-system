import django_filters
from django_filters import widgets
from .models import Complaint

class ComplaintFilter(django_filters.FilterSet):
    failure_date = django_filters.DateFromToRangeFilter(
        label='Дата отказа (от - до)',
        widget=widgets.RangeWidget(attrs={'type': 'date'})
    )
    operating_hours = django_filters.RangeFilter(
        label='Наработка (от - до)'
    )
    failure_node__name = django_filters.CharFilter(
        label='Узел отказа',
        lookup_expr='icontains'
    )
    failure_node_description = django_filters.CharFilter(
        label='Описание отказа',
        lookup_expr='icontains'
    )
    status = django_filters.ChoiceFilter(
        label='Статус',
        choices=Complaint.STATUS
    )
    service_company__name = django_filters.CharFilter(
        label='Сервисная компания',
        lookup_expr='icontains'
    )
    machine__factory_number = django_filters.CharFilter(
        label='Зав. № машины',
        lookup_expr='icontains'
    )

    class Meta:
        model = Complaint
        fields = []
