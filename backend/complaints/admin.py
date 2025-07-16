from django.contrib import admin

from . import models

admin.site.register(models.FailureNode)
admin.site.register(models.RecoveryMethod)
admin.site.register(models.Complaint)