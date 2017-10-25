from django.db import models
from apps.tables.models import Table



class Order(models.Model):
    number = models.CharField(max_length=7, blank=True, null=True)
    date = models.DateField()
    name = models.CharField(max_length=155)
    email = models.EmailField()
    ordered_tables = models.ManyToManyField(Table, related_name='table_order_check')

    def __str__(self):
        return str(self.id)

# Create your models here.


