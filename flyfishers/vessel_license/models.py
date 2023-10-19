from django.db import models

# Create your models here.
class VesselLicense(models.Model):
    vessel_license_id = models.AutoField(primary_key=True)
    type_of_vessel = models.CharField(db_column='type of vessel', max_length=45)  # Field renamed to remove unsuitable characters.
    license_type = models.CharField(db_column='license type', max_length=45)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'vessel_license'
