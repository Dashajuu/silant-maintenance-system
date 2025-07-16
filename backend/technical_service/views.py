from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView


from .forms import MaintenanceCreationForm
from . import models
from machines.forms import make_reference_item_form


# Create views
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


# Update views
class MaintenanceTypeUpdateView(UpdateView):
    model = models.MaintenanceType
    form_class = make_reference_item_form(model)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')


# Report from service on maintenance request
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


 # Edit maintenance user request by client
class MaintenanceRequestUpdateView(UpdateView):
    model = models.Maintenance
    form_class = MaintenanceCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = False
        return kwargs


class BackdateMaintenanceUpdateView(UpdateView):
    model = models.Maintenance
    form_class = MaintenanceCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['show_service_fields'] = False
        kwargs['show_request_fields'] = True
        return kwargs


# Delete views
class MaintenanceTypeDeleteView(DeleteView):
    model = models.MaintenanceType
    template_name = 'machines/delete_machine.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')


class MaintenanceDeleteView(DeleteView):
    model = models.Maintenance
    template_name = 'machines/delete_machine.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')


# TODO: добавить разные вьюшки для бэкдейт и просто заявки
# Detail views
class MaintenanceTypeDetailView(DetailView):
    model = models.MaintenanceType
    template_name = 'machines/item_detail.html'
    context_object_name = 'item'


class MaintenanceDetailView(DetailView):
    model = models.Maintenance
    template_name = 'technical_service/maintenance_detail.html'
    context_object_name = 'maintenance'


# List views
class MaintenanceTypeListView(ListView):
    model = models.MaintenanceType
    template_name = 'machines/item_list.html'
    context_object_name = 'items'


class MaintenanceListView(ListView):
    model = models.Maintenance
    template_name = 'technical_service/maintenance_list.html'
    context_object_name = 'maintenances'
