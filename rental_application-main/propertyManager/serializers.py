from rest_framework import serializers
from accounts.serializers import OwnerSerializer
from .models import PropertyDetail
from accounts.models import User


class ProperySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetail
        exclude='owner',
    
class CurrentUserPropertySerialzer(serializers.ModelSerializer):
    property = ProperySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'property']
