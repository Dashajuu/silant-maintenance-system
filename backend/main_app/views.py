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
