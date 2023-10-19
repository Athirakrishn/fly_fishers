from django.db import models
from fishermen.models import Fishermen

# Create your models here.
class Vessel(models.Model):
    vessel_id = models.AutoField(primary_key=True)
    fishermen_id = models.IntegerField()
    fishermen_name = models.CharField(db_column='fishermen name', max_length=45)  # Field renamed to remove unsuitable characters.
    name_of_vessel = models.CharField(db_column='name of vessel', max_length=45)  # Field renamed to remove unsuitable characters.
    register_no = models.IntegerField(db_column='register no')  # Field renamed to remove unsuitable characters.
    license_no = models.IntegerField(db_column='license no')  # Field renamed to remove unsuitable characters.
    crew = models.IntegerField()
    year = models.IntegerField()
    register_date = models.DateField(db_column='register date')  # Field renamed to remove unsuitable characters.
    register_place = models.CharField(db_column='register place', max_length=45)  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=45)
    detailed_description = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'vessel'
