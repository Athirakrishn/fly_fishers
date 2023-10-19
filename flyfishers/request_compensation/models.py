from django.db import models
from compensation.models import Compensation
from fishermen.models import Fishermen
# Create your models here.
class ReqCompensation(models.Model):
    req_compensation_id = models.AutoField(primary_key=True)
    # compensation_id = models.IntegerField()
    compensation=models.ForeignKey(Compensation,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    user_name = models.CharField(db_column='user name', max_length=45)  # Field renamed to remove unsuitable characters.
    reason = models.CharField(max_length=45)
    proof = models.CharField(max_length=45)
    date = models.DateField()
    status = models.CharField(max_length=45)
    details = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'req_compensation'
