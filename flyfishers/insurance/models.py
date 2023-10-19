from django.db import models

# Create your models here.

class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    insurance_name = models.CharField(db_column='insurance name', max_length=45)  # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'insurance'

