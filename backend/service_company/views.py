from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from .forms import ServiceCompanyForm
from .models import ServiceCompany


# Create views
class ServiceCompanyCreateView(CreateView):
    form_class = ServiceCompanyForm
    template_name = 'service_company/service_company_create.html'
    success_url = reverse_lazy('list_managers')


# Update views
class ServiceCompanyUpdateView(UpdateView):
    model = ServiceCompany
    form_class = ServiceCompanyForm
    template_name = 'service_company/service_company_create.html'
    success_url = reverse_lazy('list_managers')


# Delete views
class ServiceCompanyDeleteView(DeleteView):
    model = ServiceCompany
    template_name = 'service_company/service_company_create.html'
    context_object_name = 'service_company_delete'
    success_url = reverse_lazy('list_managers')


# Detail views
class ServiceCompanyDetailView(DetailView):
    model = ServiceCompany
    template_name = 'service_company/service_company_detail.html'
    context_object_name = 'service_company'


# List views
class ServiceCompanyListView(ListView):
    model = ServiceCompany
    template_name = 'service_company/service_company_list.html'
    context_object_name = 'service_companies'
