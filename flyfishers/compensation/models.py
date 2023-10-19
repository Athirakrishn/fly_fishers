from django.db import models

# Create your models here.

class Compensation(models.Model):
    compensation_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    amount = models.IntegerField()
    rules = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'compensation'
