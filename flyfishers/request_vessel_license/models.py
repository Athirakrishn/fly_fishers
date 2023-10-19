from django.db import models
from vessel_license.models import VesselLicense
from fishermen.models import Fishermen
from vessel.models import Vessel
# Create your models here.
class ReqVesselLicense(models.Model):
    req_vessel_license_id = models.AutoField(primary_key=True)
    # vessel_license_id = models.IntegerField()
    vessel_license=models.ForeignKey(VesselLicense,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    vessel_no = models.IntegerField(db_column='vessel no')  # Field renamed to remove unsuitable characters.
    request = models.CharField(max_length=45)
    id_proof = models.CharField(db_column='id proof', max_length=45)  # Field renamed to remove unsuitable characters.
    manifacture_date = models.DateField(db_column='manifacture date')  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'req_vessel_license'

