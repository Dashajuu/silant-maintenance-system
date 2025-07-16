from django.contrib import admin

from . import models


admin.site.register(models.MaintenanceType)
admin.site.register(models.Maintenance)
