from rest_framework import serializers
from .models import Property
from rest_framework import serializers


class propertyserializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
