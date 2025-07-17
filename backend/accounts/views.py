from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

from .forms import ManagerCreationForm, ClientCreationForm, ServiceMasterCreationForm, ContactPersonCreationForm, make_custom_update_form, LoginForm
from .models import Manager, Client, ServiceMaster, ContactPerson
from service_company.models import ServiceCompany


# TODO: change name or delete
def account_creation_home(request):
    return render(request, "accounts/account_creation_main.html")


# Create view
class ManagerCreateView(CreateView):
    form_class = ManagerCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('list_managers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта менеджера'
        return context


class ClientCreateView(CreateView):
    form_class = ClientCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта клиента'
        return context


class ServiceMasterCreateView(CreateView):
    form_class = ServiceMasterCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта мастера сервисной компании'
        return context


class ContactPersonCreateView(CreateView):
    form_class = ContactPersonCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта контактного лица сервисной компании'
        return context


# Update views
class ManagerUpdateView(UpdateView):
    model = Manager
    form_class = make_custom_update_form(model, 'region')
    template_name = 'accounts/accounts_create.html'

    def get_success_url(self):
        return reverse_lazy('manager_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта менеджера: {self.object.user.username}'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = make_custom_update_form(model, 'name')
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта клиента: {self.object.user.username}'
        return context


class ServiceMasterUpdateView(UpdateView):
    model = ServiceMaster
    form_class = make_custom_update_form(model, 'position', 'service_company')
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта мастера: {self.object.user.username}'
        return context


class ContactPersonUpdateView(UpdateView):
    model = ContactPerson
    form_class = make_custom_update_form(model, 'service_company')
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта контактного лица: {self.object.user.username}'
        return context


# Delete views
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accounts/accounts_confirm_delete.html'
    success_url = reverse_lazy('create_account')


# TODO: пересмотреть шаблоны
# Detail views
class ManagerProfileDetailView(DetailView):
    model = Manager
    template_name = 'accounts/accounts_manager_detail.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(Q(manager=self.object) | Q(manager=1))
        context['service_companies'] = ServiceCompany.objects.all()
        return context


class ClientProfileDetailView(DetailView):
    model = Client
    template_name = 'accounts/accounts_detail.html'
    context_object_name = 'account'


class ServiceMasterProfileDetailView(DetailView):
    model = ServiceMaster
    template_name = 'accounts/accounts_detail.html'
    context_object_name = 'account'


class ContactPersonProfileDetailView(DetailView):
    model = ContactPerson
    template_name = 'accounts/accounts_detail.html'
    context_object_name = 'account'


# List views
class ManagerListView(ListView):
    model = Manager
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ClientListView(ListView):
    model = Client
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ServiceMasterListView(ListView):
    model = ServiceMaster
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ContactPersonListView(ListView):
    model = ContactPerson
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class CustomLoginView(LoginView):
    authentication_form = LoginForm
