from django.db import models
from fishermen.models import Fishermen
# Create your models here.
class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(db_column='equipment name', max_length=45)  # Field renamed to remove unsuitable characters.
    equipmentimage = models.CharField(max_length=500)
    quandity = models.IntegerField()
    subsidy = models.CharField(max_length=45)
    price = models.IntegerField()
    status = models.CharField(max_length=45)
    fishermen = models.ForeignKey(Fishermen,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'equipment'



