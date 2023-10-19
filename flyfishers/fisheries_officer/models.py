from django.db import models

# Create your models here.

class FisheriesOfficer(models.Model):
    fisheries_officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    date_of_birth = models.DateField(db_column='date of birth')  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    contact_no = models.CharField(db_column='contact no', max_length=30)  # Field renamed to remove unsuitable characters.
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'fisheries_officer'

