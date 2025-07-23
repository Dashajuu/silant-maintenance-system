import django_filters

from .models import Maintenance


class MaintenanceFilter(django_filters.FilterSet):
    maintenance_type = django_filters.CharFilter(label='Вид ТО', lookup_expr='icontains')
    maintenance_date = django_filters.DateFromToRangeFilter(label='Дата ТО (от - до)', widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    operating_hours = django_filters.RangeFilter(label='Наработка (от - до)')
    work_order_number = django_filters.CharFilter(label='Номер заказ-наряда', lookup_expr='icontains')
    work_order_date = django_filters.DateFromToRangeFilter(label='Дата заказ-наряда (от - до)', widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    service_company = django_filters.CharFilter(label='Сервисная компания', lookup_expr='icontains')
    status = django_filters.ChoiceFilter(label='Статус', choices=Maintenance.STATUS)

    class Meta:
        model = Maintenance
        fields = []