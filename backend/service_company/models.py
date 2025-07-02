from django.db import models


class ServiceCompany(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
