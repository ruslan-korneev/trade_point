from django.db import models

from apps.employees.models import Employee


class Store(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Visit(models.Model):
    visit_date = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def store_and_employee(self):
        return f"{self.store.title} - {self.store.employee.name}"
