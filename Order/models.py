from django.db import models
from Customer.models import  Customer
from Employee.models import Employee
from Shipper.models import Shipper
from datetime import datetime 
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(default=datetime.now)
