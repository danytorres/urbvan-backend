from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)