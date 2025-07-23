from rest_framework import serializers

from . import models


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCompany
        fields = '__all__'


class ServiceMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceMaster
        fields = '__all__'


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactPerson
        fields = '__all__'
