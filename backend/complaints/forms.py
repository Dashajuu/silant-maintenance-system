from django import forms

from . import models


class ComplaintCreationForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        show_service_fields = kwargs.pop('show_service_fields', False)
        super().__init__(*args, **kwargs)

        if not show_service_fields:
            for field_name in ['recovery_method', 'used_spare_parts', 'recovery_date', 'downtime']:
                self.fields.pop(field_name)
