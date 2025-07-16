from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView,
                                  ListView, DetailView)

from .forms import ComplaintCreationForm
from . import models
from machines.forms import make_reference_item_form


# TODO: пересмотреть шаблоны - изменить или сделать дефолтные для всех

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
    model = models.Complaint
    form_class = ComplaintCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs


class BackdateComplaintUpdateView(UpdateView):
    model = models.Complaint
    form_class = ComplaintCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs


class FailureNodeUpdateView(UpdateView):
    model = models.FailureNode
    form_class = make_reference_item_form(model)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')


class RecoveryMethodUpdateView(UpdateView):
    model = models.RecoveryMethod
    form_class = make_reference_item_form(model)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')


# Delete views
class ComplaintDeleteView(DeleteView):
    model = models.Complaint
    template_name = 'machines/delete_machine.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')


class FailureNodeDeleteView(DeleteView):
    model = models.FailureNode
    template_name = 'machines/delete_machine.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')


class RecoveryMethodDeleteView(DeleteView):
    model = models.RecoveryMethod
    template_name = 'machines/delete_machine.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')


# TODO: maybe add backdate complaint
# Detail views
class FailureNodeDetailView(DetailView):
    model = models.FailureNode
    template_name = 'complaints/detail_complaint.html'
    context_object_name = 'complaint'


class RecoveryMethodDetailView(DetailView):
    model = models.RecoveryMethod
    template_name = 'complaints/detail_complaint.html'
    context_object_name = 'complaint'


class ComplaintDetailView(DetailView):
    model = models.Complaint
    template_name = 'complaints/detail_complaint.html'
    context_object_name = 'complaint'


# List views
class FailureNodeListView(ListView):
    model = models.FailureNode
    template_name = 'complaints/list_complaint.html'
    context_object_name = 'complaints'


class RecoveryMethodListView(ListView):
    model = models.RecoveryMethod
    template_name = 'complaints/list_complaint.html'
    context_object_name = 'complaints'


class ComplaintListView(ListView):
    model = models.Complaint
    template_name = 'complaints/list_complaint.html'
    context_object_name = 'complaints'
