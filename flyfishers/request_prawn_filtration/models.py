from django.db import models
from prawn_filtration.models import PrawnFiltration
from fishermen.models import Fishermen
# Create your models here.
class ReqPrawnFiltration(models.Model):
    req_prawn_filtration_id = models.AutoField(primary_key=True)
    # prawn_filtration_id = models.IntegerField()
    prawn_filtration=models.ForeignKey(PrawnFiltration,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    license_no = models.IntegerField(db_column='license no')  # Field renamed to remove unsuitable characters.
    request = models.CharField(max_length=400)
    date = models.DateField()
    status = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'req_prawn_filtration'
