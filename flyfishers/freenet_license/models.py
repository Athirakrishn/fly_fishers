from django.db import models

# Create your models here.
class FreenetLicence(models.Model):
    freenet_licence_id = models.AutoField(primary_key=True)
    type_of_net = models.CharField(db_column='type of net', max_length=45)  # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'freenet_licence'
