from django.db import models

# Create your models here.
class CustomManager1(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset().filter(esal__gt=30000)
        return qs
    
class CustomManager2(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset().filter(ename__startswith='b')
        return qs
    
class CustomManager3(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset().order_by('-eno')
        return qs


class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=40)
    objects=CustomManager1()

class ProxyEmployee1(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee2(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True