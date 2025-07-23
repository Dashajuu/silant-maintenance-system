from rest_framework import serializers
from . import models


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = '__all__'


class FailureNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FailureNode
        fields = '__all__'


class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecoveryMethod
        fields = '__all__'
