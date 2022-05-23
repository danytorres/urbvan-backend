from employees.models import Employee
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'