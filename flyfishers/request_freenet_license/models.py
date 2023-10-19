from django.db import models
from freenet_license.models import FreenetLicence
from fishermen.models import Fishermen

class ReqFreenetLicense(models.Model):
    req_freenet_license_id = models.AutoField(primary_key=True)
    fishermen_id = models.IntegerField()
    # fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=45)
    # freenet_licence_id = models.IntegerField()
    freenet_licence=models.ForeignKey(FreenetLicence,on_delete=models.CASCADE)
    id_proof = models.CharField(max_length=45)
    more_details = models.CharField(max_length=400)
    class Meta:
        managed = False
        db_table = 'req_freenet_license'
