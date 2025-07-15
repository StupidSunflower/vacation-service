from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id = models.IntegerField(unique=True)
    department_id = models.IntegerField(default=0)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    vacation_days = models.IntegerField(default=0)
    date_of_employment = models.DateField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'employee'
        managed = True

class Vacation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'vacation'
        managed = True
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lte=models.F('end_date')),
                name='valid_vacation_dates'
            )
        ]