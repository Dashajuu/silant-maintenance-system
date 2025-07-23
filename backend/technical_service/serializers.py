from rest_framework import serializers
from . import models


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maintenance
        fields = '__all__'


class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceType
        fields = '__all__'
