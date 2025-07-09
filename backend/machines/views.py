from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import make_reference_item_form
from . import models


class MachineTypeCreateView(CreateView):
    form_class = make_reference_item_form(models.MachineType)
    template_name = 'machines/create_machine.html'
    success_url = reverse_lazy('home_page')