import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proxymodel.settings')

import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake=Faker()

def populate(n):
    for i in range(n):
        feno=randint(1,100)
        fename=fake.name()
        fesal=randint(10000,50000)
        feaddr=fake.city()
        emp_records=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            eaddr=feaddr
        )
n=int(input('Enter number of records you want = '))
populate(n)
print(f'{n} records inserted into database')