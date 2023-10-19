from django.db import models

# Create your models here.
class ReliefSchem(models.Model):
    relief_schem_id = models.AutoField(primary_key=True)
    scheme_name = models.CharField(db_column='scheme name', max_length=100)  # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'relief_schem'



