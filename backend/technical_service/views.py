from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


from .forms import MaintenanceCreationForm
from . import models
from machines.forms import make_reference_item_form


# Create view
class MaintenanceTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.MaintenanceType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вид ТО'
        return context


class BackdateMaintenanceCreateView(CreateView):
    form_class = MaintenanceCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = 'closed'
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = True
        return kwargs


class MaintenanceCreateView(CreateView):
    form_class = MaintenanceCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = 'new'
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = False
        return kwargs


# Update view
class ServiceMaintenanceUpdateView(UpdateView):
    form_class = MaintenanceCreationForm
    model = models.Maintenance
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        kwargs['show_request_fields'] = True
        return kwargs
