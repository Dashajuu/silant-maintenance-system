from django import forms

from .models import ServiceCompany


class ServiceCompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=150, label="Название компании")
    description = forms.CharField(widget=forms.Textarea, label="Описание компании (адрес, часы работы)", required=False)

    class Meta:
        model = ServiceCompany
        fields = ['name', 'description']