from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ManagerCreationForm
from .models import Manager


class ManagerListView(ListView):
    model = Manager
    context_object_name = 'managers'
    template_name = 'accounts/manager-list.html'


class ManagerCreateView(CreateView):
    form_class = ManagerCreationForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('list_managers')

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)

