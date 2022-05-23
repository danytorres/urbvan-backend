from rest_framework import viewsets
from rest_framework import permissions
from employees.serializers import UserSerializer
from employees.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]