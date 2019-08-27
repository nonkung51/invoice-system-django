from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    tax_id = models.CharField(max_length=25)
    address = models.CharField(max_length=500)
    id_number = models.CharField(max_length=20)

    def __str__(self):
        return self.id_number