from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User

from .forms import ManagerCreationForm, ClientCreationForm, ServiceMasterCreationForm, ContactPersonCreationForm, make_custom_update_form
from .models import Manager, Client, ServiceMaster, ContactPerson


# TODO: change name or delete
def account_creation_home(request):
    return render(request, "accounts/account_creation_main.html")


# TODO: unnecessary, delete later
class ManagerListView(ListView):
    model = Manager
    context_object_name = 'managers'
    template_name = 'accounts/manager-list.html'


# Create view
class ManagerCreateView(CreateView):
    form_class = ManagerCreationForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('list_managers')


class ClientCreateView(CreateView):
    form_class = ClientCreationForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


class ServiceMasterCreateView(CreateView):
    form_class = ServiceMasterCreationForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


class ContactPersonCreateView(CreateView):
    form_class = ContactPersonCreationForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


# Update views
class ManagerUpdateView(UpdateView):
    model = Manager
    form_class = make_custom_update_form(model, 'region')
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = make_custom_update_form(model, 'name')
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


class ServiceMasterUpdateView(UpdateView):
    model = ServiceMaster
    form_class = make_custom_update_form(model, 'position', 'service_company')
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')


class ContactPersonUpdateView(UpdateView):
    model = ContactPerson
    form_class = make_custom_update_form(model, 'service_company')
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('create_account')
