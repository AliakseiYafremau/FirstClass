from rest_framework import serializers
from .models import *

# Сериализатор для модели Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client
