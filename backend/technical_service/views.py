from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView


from .forms import MaintenanceCreationForm
from . import models
from machines.forms import make_reference_item_form


# Create views
class MaintenanceTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.MaintenanceType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.add_maintenancetype'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вид ТО'
        return context


class BackdateMaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MaintenanceCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.add_maintenance'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = 'closed'
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = True
        return kwargs


class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MaintenanceCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.add_maintenance'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = 'new'
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = False
        return kwargs


# Update views
class MaintenanceTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.MaintenanceType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.change_maintenancetype'


# Report from service on maintenance request
class ServiceMaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = MaintenanceCreationForm
    model = models.Maintenance
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.change_maintenance'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = True
        kwargs['show_request_fields'] = True
        return kwargs


 # Edit maintenance user request by client
class MaintenanceRequestUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Maintenance
    form_class = MaintenanceCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.change_maintenance'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = False
        return kwargs


class BackdateMaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Maintenance
    form_class = MaintenanceCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.change_maintenance'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = True
        return kwargs


# Delete views
class MaintenanceTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.MaintenanceType
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.delete_maintenancetype'


class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Maintenance
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'technical_service.delete_maintenance'


# TODO: добавить разные вьюшки для бэкдейт и просто заявки
# Detail views
class MaintenanceTypeDetailView(LoginRequiredMixin, DetailView):
    model = models.MaintenanceType
    template_name = 'technical_service/technical_service_maintenance_type.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вид ТО'
        context['items_name'] = 'maintenance_type'
        return context


class MaintenanceDetailView(LoginRequiredMixin, DetailView):
    model = models.Maintenance
    template_name = 'technical_service/technical_service_detail.html'
    context_object_name = 'maintenance'


# List views
class MaintenanceTypeListView(LoginRequiredMixin, ListView):
    model = models.MaintenanceType
    template_name = 'machines/machines_items_list.html'
    context_object_name = 'items'


class MaintenanceListView(LoginRequiredMixin, ListView):
    model = models.Maintenance
    template_name = 'technical_service/technical_service_list.html'
    context_object_name = 'maintenances'
