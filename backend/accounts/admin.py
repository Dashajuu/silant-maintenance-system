from django.contrib import admin

from . import models

admin.site.register(models.ServiceMaster)
admin.site.register(models.ContactPerson)
admin.site.register(models.Manager)
admin.site.register(models.Client)