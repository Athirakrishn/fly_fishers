from django.db import models

# Create your models here.

class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'alert'
