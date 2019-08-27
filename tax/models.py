from django.db import models

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=50)
    people_id = models.CharField(max_length=20)
    proving_state = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Field(models.Model):
    field_name = models.CharField(max_length=50)
    field_value = models.PositiveIntegerField(default=0)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill.name + " " + self.field_name