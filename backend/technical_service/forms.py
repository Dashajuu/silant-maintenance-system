from django import forms

from .models import Maintenance


class MaintenanceCreationForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        show_service_fields = kwargs.pop('show_service_fields', False)
        show_request_fields = kwargs.pop('show_request_fields', False)
        super().__init__(*args, **kwargs)

        if not show_service_fields:
            for field_name in ['service_company_respond', 'complaint_number', 'service_master']:
                self.fields.pop(field_name)

        if not show_request_fields:
            for field_name in ['maintenance_type', 'maintenance_date', 'work_order_number',
                               'work_order_date', 'service_company', 'status']:
                self.fields.pop(field_name)
