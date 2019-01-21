from rest_framework import serializers
from . import models


class RadPostAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RadPostAuth
        fields = '__all__'


class RadCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RadCheck
        fields = '__all__'


class RadUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RadUserGroup
        fields = '__all__'
