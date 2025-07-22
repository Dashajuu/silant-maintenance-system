from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView,
                                  ListView, DetailView)

from .forms import ComplaintCreationForm
from . import models
from machines.forms import make_reference_item_form


# Create view
class FailureNodeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.FailureNode)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.add_failurenode'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Узел отказа'
        return context


class RecoveryMethodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.RecoveryMethod)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.add_recoverymethod'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Способ восстановления'
        return context


class ComplaintCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ComplaintCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.add_complaint'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        return kwargs


class BackdateComplaintCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ComplaintCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.add_complaint'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs



# Update view
class ComplaintUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Complaint
    form_class = ComplaintCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.change_complaint'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs


class BackdateComplaintUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Complaint
    form_class = ComplaintCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.change_complaint'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        return kwargs


class FailureNodeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.FailureNode
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.change_failurenode'


class RecoveryMethodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.RecoveryMethod
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.change_recoverymethod'


# Delete views
class ComplaintDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Complaint
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.delete_complaint'


class FailureNodeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.FailureNode
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.delete_failurenode'


class RecoveryMethodDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.RecoveryMethod
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'complaints.delete_recoverymethod'


# TODO: maybe add backdate complaint
# Detail views
class FailureNodeDetailView(LoginRequiredMixin, DetailView):
    model = models.FailureNode
    template_name = 'complaints/complaints_detail.html'
    context_object_name = 'complaint'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Узел отказа'
        context['items_name'] = 'failure_node'
        return context


class RecoveryMethodDetailView(LoginRequiredMixin, DetailView):
    model = models.RecoveryMethod
    template_name = 'complaints/complaints_detail.html'
    context_object_name = 'complaint'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Способ восстановления'
        context['items_name'] = 'recovery_method'
        return context


class ComplaintDetailView(LoginRequiredMixin, DetailView):
    model = models.Complaint
    template_name = 'complaints/complaints_detail.html'
    context_object_name = 'complaint'


# List views
class FailureNodeListView(LoginRequiredMixin, ListView):
    model = models.FailureNode
    template_name = 'complaints/complaints_list.html'
    context_object_name = 'complaints'


class RecoveryMethodListView(LoginRequiredMixin, ListView):
    model = models.RecoveryMethod
    template_name = 'complaints/complaints_list.html'
    context_object_name = 'complaints'


class ComplaintListView(LoginRequiredMixin, ListView):
    model = models.Complaint
    template_name = 'complaints/complaints_list.html'
    context_object_name = 'complaints'
