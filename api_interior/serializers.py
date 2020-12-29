from rest_framework import serializers
from .models import interior , login
from phone_field import PhoneField


class interiorSerializer(serializers.ModelSerializer):
    class Meta:
        model = interior
        fields = ['id', 'name', 'email', 'phoneno', 'message']

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ['username','password']