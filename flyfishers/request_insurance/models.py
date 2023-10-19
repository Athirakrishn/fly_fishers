
from django.db import models
from insurance.models import Insurance
from fishermen.models import Fishermen
from vessel.models import Vessel
# Create your models here.
class ReqInsurance(models.Model):
    req_insurance_id = models.AutoField(primary_key=True)
    # insurance_id = models.IntegerField()
    insurance=models.ForeignKey(Insurance,on_delete=models.CASCADE)
    # vessel_id = models.IntegerField()
    vessel=models.ForeignKey(Vessel,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    id_proof = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'req_insurance'
