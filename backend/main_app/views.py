from django.shortcuts import render

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
