from django.db import models
from equipment.models import Equipment
from fishermen.models import Fishermen

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # equipment_id = models.IntegerField()
    equipment=models.ForeignKey(Equipment,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    subcidy = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order'


