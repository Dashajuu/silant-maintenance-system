from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ServiceCompanyForm
from .models import ServiceCompany


class ServiceCompanyCreateView(CreateView):
    form_class = ServiceCompanyForm
    template_name = 'service_company/service_company_creation.html'
    success_url = reverse_lazy('list_managers')
