from django.db import models

# Create your models here.
class PrawnFiltration(models.Model):
    prawn_filtration_id = models.AutoField(primary_key=True)
    available_date = models.CharField(db_column='available date', max_length=45)  # Field renamed to remove unsuitable characters.
    details = models.CharField(db_column='Details', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prawn_filtration'

