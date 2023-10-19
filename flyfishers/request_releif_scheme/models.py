from django.db import models
from relief_scheme.models import ReliefSchem
from fishermen.models import Fishermen
# Create your models here.
class ReqReliefScheme(models.Model):
    req_relief_schem_id = models.AutoField(primary_key=True)
    # relief_schem_id = models.IntegerField()
    relief_schem=models.ForeignKey(ReliefSchem,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    id_proof = models.CharField(db_column='id proof', max_length=45)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'req_relief_scheme'

