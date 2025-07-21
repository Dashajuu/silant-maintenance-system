from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

from .forms import ManagerCreationForm, ClientCreationForm, ServiceMasterCreationForm, ContactPersonCreationForm, make_custom_update_form, LoginForm, ServiceCompanyCreationForm
from .models import Manager, Client, ServiceMaster, ContactPerson, ServiceCompany
from machines.models import Machine


# TODO: change name or delete
def account_creation_home(request):
    return render(request, "accounts/account_creation_main.html")


# Create view
class ManagerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ManagerCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('list_managers')
    permission_required = 'accounts.add_manager'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта менеджера'
        return context


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ClientCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.add_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта клиента'
        return context


class ServiceMasterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ServiceMasterCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.add_service_master'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта мастера сервисной компании'
        return context


class ContactPersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ContactPersonCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.add_contact_person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта контактного лица сервисной компании'
        return context


class ServiceCompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ServiceCompanyCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.add_service_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание аккаунта сервисной компании'
        return context


# Update views
class ManagerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Manager
    form_class = make_custom_update_form(model, 'region')
    template_name = 'accounts/accounts_create.html'
    permission_required = 'accounts.change_manager'

    def get_success_url(self):
        return reverse_lazy('manager_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта менеджера: {self.object.user.username}'
        return context


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = make_custom_update_form(model, 'name')
    template_name = 'accounts/accounts_create.html'
    permission_required = 'accounts.change_client'

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта клиента: {self.object.user.username}'
        return context


class ServiceMasterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ServiceMaster
    form_class = make_custom_update_form(model, 'position', 'service_company')
    template_name = 'accounts/accounts_create.html'
    permission_required = 'accounts.change_service_master'

    def get_success_url(self):
        return reverse_lazy('service_master_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта мастера: {self.object.user.username}'
        return context


class ContactPersonUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ContactPerson
    form_class = make_custom_update_form(model, 'service_company')
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.change_contact_person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта контактного лица: {self.object.user.username}'
        return context


class ServiceCompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ServiceCompany
    form_class = make_custom_update_form(model, 'name', 'description')
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.change_service_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование аккаунта сервисной компании: {self.object.user.username}'
        return context


# Delete views
class AccountDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/accounts_confirm_delete.html'
    success_url = reverse_lazy('create_account')
    permission_required = 'accounts.delete_account'


# Detail views
class ManagerProfileDetailView(LoginRequiredMixin, DetailView):
    model = Manager
    template_name = 'accounts/accounts_manager_detail.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(Q(manager=self.object) | Q(manager=1))
        context['service_companies'] = ServiceCompany.objects.all()
        return context


class ClientProfileDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'accounts/accounts_client_detail.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.filter(client=self.object)
        service_company_ids = Machine.objects.filter(client=self.object).values_list('service_company',
                                                                                     flat=True).distinct()
        context['service_companies'] = ServiceCompany.objects.filter(id__in=service_company_ids)

        return context


class ServiceMasterProfileDetailView(LoginRequiredMixin, DetailView):
    model = ServiceMaster
    template_name = 'accounts/accounts_service_master_detail.html'
    context_object_name = 'account'


# TODO: add profile page + template
class ContactPersonProfileDetailView(LoginRequiredMixin, DetailView):
    model = ContactPerson
    template_name = 'accounts/accounts_service_master_detail.html'
    context_object_name = 'account'


# TODO: add profile page + template
class ServiceCompanyProfileDetailView(LoginRequiredMixin, DetailView):
    model = ServiceCompany
    template_name = 'accounts/accounts_service_master_detail.html'
    context_object_name = 'account'


# List views
class ManagerListView(LoginRequiredMixin, ListView):
    model = Manager
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ServiceMasterListView(LoginRequiredMixin, ListView):
    model = ServiceMaster
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ContactPersonListView(LoginRequiredMixin, ListView):
    model = ContactPerson
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class ServiceCompanyListView(LoginRequiredMixin, ListView):
    model = ServiceCompany
    context_object_name = 'accounts'
    template_name = 'accounts/accounts-list.html'


class CustomLoginView(LoginView):
    authentication_form = LoginForm
