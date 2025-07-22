from django.http import HttpResponse
from django.template.loader import render_to_string
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .forms import make_reference_item_form, MachineCreationForm
from . import models
from .filters import MachineFilter

from technical_service.models import Maintenance
from complaints.models import Complaint


# Create view
class MachineTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.MachineType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_machine_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель техники'
        return context


class EngineTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.EngineType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_engine_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель двигателя'
        return context


class TransmissionTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.TransmissionType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_transmission_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель трансмиссии'
        return context


class DriveAxleTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.DriveAxleType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_drive_axle_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель ведущего моста'
        return context


class SteerAxleTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = make_reference_item_form(models.SteerAxleType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_steer_axle_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель управляемого моста'
        return context


class MachineCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MachineCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.add_machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Машина'
        return context


# Update views
class MachineTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.MachineType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_machine_type'


class EngineTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.EngineType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_engine_type'


class TransmissionTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TransmissionType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_transmission_type'


class DriveAxleTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.DriveAxleType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_drive_axle_type'


class SteerAxleTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.SteerAxleType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_steer_axle_type'


class MachineUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Machine
    form_class = MachineCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.change_machine'


# Delete views
def delete_item_view(machine_model, permission_name):
    class ItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
        model = machine_model
        template_name = 'machines/machines_confirm_delete.html'
        context_object_name = 'machine_delete'
        success_url = reverse_lazy('home_page')
        permission_required = f'machines.delete_{permission_name}'

    return ItemDeleteView


class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Machine
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')
    permission_required = 'machines.delete_machine'



# Detail views

# factory function for items' detail views
def create_detail_view(item_model, item_template_name, item_context_object_name, title_name, items_name):
    class ItemDetailView(LoginRequiredMixin, DetailView):
        model = item_model
        template_name = item_template_name
        context_object_name = item_context_object_name

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = title_name
            context['items_name'] = items_name
            return context

    return ItemDetailView


class MachineDetailView(LoginRequiredMixin, DetailView):
    model = models.Machine
    template_name = 'machines/machines_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maintenances'] = Maintenance.objects.filter(machine=self.object)
        context['complaints'] = Complaint.objects.filter(machine=self.object)
        return context


# List view

# factory function for items' list views
def create_list_view(item_model, item_template_name, item_context_object_name):
    class ItemListView(LoginRequiredMixin, DetailView):
        model = item_model
        template_name = item_template_name
        context_object_name = item_context_object_name
    return ItemListView


class MachineListView(ListView):
    model = models.Machine
    template_name = 'machines/machines_list.html'
    context_object_name = 'machines'
    ordering = ['-shipment_date']
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('machines/machine_result_partial.html', context)
            return HttpResponse(html)
        else:
            return super().render_to_response(context, **response_kwargs)