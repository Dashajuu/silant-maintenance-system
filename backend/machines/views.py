from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import make_reference_item_form, MachineCreationForm
from . import models


# Create view

class MachineTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.MachineType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель техники'
        return context


class EngineTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.EngineType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель двигателя'
        return context


class TransmissionTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.TransmissionType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель трансмиссии'
        return context

class DriveAxleTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.DriveAxleType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель ведущего моста'
        return context


class SteerAxleTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.SteerAxleType)
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Модель управляемого моста'
        return context


class MachineCreateView(CreateView):
    form_class = MachineCreationForm
    template_name = 'machines/create_machine_item.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Машина'
        return context
