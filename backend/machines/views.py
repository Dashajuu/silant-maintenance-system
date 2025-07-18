from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from .forms import make_reference_item_form, MachineCreationForm
from . import models
from .filters import MachineFilter


# Create view
# TODO: норм ли сделать функцию фабрику для крад вьюшек?
class MachineTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.MachineType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель техники'
        return context


class EngineTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.EngineType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель двигателя'
        return context


class TransmissionTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.TransmissionType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель трансмиссии'
        return context


class DriveAxleTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.DriveAxleType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель ведущего моста'
        return context


class SteerAxleTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.SteerAxleType)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель управляемого моста'
        return context


class MachineCreateView(CreateView):
    form_class = MachineCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Машина'
        return context


# Update views
class MachineTypeUpdateView(UpdateView):
    model = models.MachineType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


class EngineTypeUpdateView(UpdateView):
    model = models.EngineType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


class TransmissionTypeUpdateView(UpdateView):
    model = models.TransmissionType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


class DriveAxleTypeUpdateView(UpdateView):
    model = models.DriveAxleType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


class SteerAxleTypeUpdateView(UpdateView):
    model = models.SteerAxleType
    form_class = make_reference_item_form(model)
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


class MachineUpdateView(UpdateView):
    model = models.Machine
    form_class = MachineCreationForm
    template_name = 'machines/machines_items_create.html'
    success_url = reverse_lazy('home_page')


# Delete views
def delete_item_view(machine_model):
    class ItemDeleteView(DeleteView):
        model = machine_model
        template_name = 'machines/machines_confirm_delete.html'
        context_object_name = 'machine_delete'
        success_url = reverse_lazy('home_page')

    return ItemDeleteView


class MachineDeleteView(DeleteView):
    model = models.Machine
    template_name = 'machines/machines_confirm_delete.html'
    context_object_name = 'machine_delete'
    success_url = reverse_lazy('home_page')



# Detail views

# factory function for items' detail views
def create_detail_view(item_model, item_template_name, item_context_object_name):
    class ItemDetailView(DetailView):
        model = item_model
        template_name = item_template_name
        context_object_name = item_context_object_name
    return ItemDetailView


class MachineDetailView(DetailView):
    model = models.Machine
    template_name = 'machines/machines_detail.html'
    context_object_name = 'machine'


# List view

# factory function for items' list views
def create_list_view(item_model, item_template_name, item_context_object_name):
    class ItemListView(DetailView):
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
