import django_filters

from .models import Machine

class MachineFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Search')


    class Meta:
        model = Machine
        fields = {
            'machine_type': ['exact'],
            'engine_type': ['exact'],
            'transmission_type': ['exact'],
            'drive_axle_type': ['exact'],
            'steer_axle_type': ['exact'],
        }


    def filter_search(self, queryset, machine_serial_number, value):
        return queryset.filter(machine_serial_number__icontains=value)