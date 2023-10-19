from django.db import models

# Create your models here.
class Fishermen(models.Model):
    fishermen_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    date_of_birth = models.DateField(db_column='date of birth')  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    contact = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    id_proof = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'fishermen'


