from django.db import models


class Hall(models.Model):
    number = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.number

class Table(models.Model):
    number = models.CharField(max_length=7, blank=True, null=True)
    shape = models.CharField(max_length=6, choices=(('oval', 'Oval'), ('square', 'Square')))
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    length = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def check_status(self, date_to):
        return self.table_order_check.filter(date=date_to).exists()
