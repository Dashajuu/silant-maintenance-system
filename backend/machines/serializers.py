from rest_framework import serializers
from . import models


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Machine
        fields = '__all__'


class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MachineType
        fields = '__all__'


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EngineType
        fields = '__all__'


class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransmissionType
        fields = '__all__'


class DriveAxleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DriveAxleType
        fields = '__all__'


class SteerAxleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SteerAxleType
        fields = '__all__'
