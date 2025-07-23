from django.http import Http404
from django.shortcuts import render

from accounts import models as account
from machines import models as machine
from technical_service import models as maintenance
from complaints import models as complaint


def get_manager_context_data(request):
    data = {
        'machine_type': machine.MachineType.objects.all(),
        'engine_type': machine.EngineType.objects.all(),
        'transmission_type': machine.TransmissionType.objects.all(),
        'drive_axle_type': machine.DriveAxleType.objects.all(),
        'steer_axle_type': machine.SteerAxleType.objects.all(),
        'maintenance_type': maintenance.MaintenanceType.objects.all(),
        'failure_nodes': complaint.FailureNode.objects.all(),
        'recovery_methods': complaint.RecoveryMethod.objects.all(),
    }

    return render(request, 'main/manager_reference_data.html', context=data)


def get_manager_accounts_context_data(request):
    data = {
        'managers': account.Manager.objects.all(),
        'clients': account.Client.objects.all(),
        'service_companies': account.ServiceCompany.objects.all(),
        'service_masters': account.ServiceMaster.objects.all(),
        'contact_persons': account.ContactPerson.objects.all(),
    }

    return render(request, 'main/manager_account_data.html', context=data)


def get_maintenance_complaints_data(request):
    user = request.user
    group = user.groups.first()

    if not group:
        raise Http404("Группа пользователя не определена")

    role = group.name
    context = {}

    if role == "managers":
        try:
            manager = account.Manager.objects.get(user=user)
            clients = account.Client.objects.filter(manager=manager)
            machines = machine.Machine.objects.filter(client__in=clients)
        except account.Manager.DoesNotExist:
            raise Http404("Менеджер не найден")

    elif role == "clients":
        try:
            client = account.Client.objects.get(user=user)
            machines = machine.Machine.objects.filter(client=client)
        except account.Client.DoesNotExist:
            raise Http404("Клиент не найден")

    elif role == "service_companies":
        try:
            service_company = account.ServiceCompany.objects.get(user=user)
            machines = machine.Machine.objects.filter(service_company=service_company)
        except account.ServiceCompany.DoesNotExist:
            raise Http404("Сервисная компания не найдена")

    else:
        raise Http404("Неизвестная роль пользователя")

    context['maintenances'] = maintenance.Maintenance.objects.filter(machine__in=machines)
    context['complaints'] = complaint.Complaint.objects.filter(machine__in=machines)

    return render(request, 'main/service.html', context)
