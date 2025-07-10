from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import ComplaintCreationForm
from . import models
from machines.forms import make_reference_item_form


# Create view
class FailureNodeCreateView(CreateView):
    form_class = make_reference_item_form(models.FailureNode)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Узел отказа'
        return context


class RecoveryMethodCreateView(CreateView):
    form_class = make_reference_item_form(models.RecoveryMethod)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Способ восстановления'
        return context


class ComplaintCreateView(CreateView):
    form_class = ComplaintCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        return kwargs


class BackdateComplaintCreateView(CreateView):
    form_class = ComplaintCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs



# Update view
class ComplaintUpdateView(UpdateView):
    form_class = ComplaintCreationForm
    model = models.Complaint
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs