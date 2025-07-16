from django.contrib import admin

from . import models


admin.site.register(models.MachineType)
admin.site.register(models.EngineType)
admin.site.register(models.TransmissionType)
admin.site.register(models.DriveAxleType)
admin.site.register(models.SteerAxleType)
admin.site.register(models.Machine)
