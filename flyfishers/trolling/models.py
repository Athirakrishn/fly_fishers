from django.db import models

# Create your models here.
class Trolling(models.Model):
    trolling_id = models.AutoField(primary_key=True)
    trolling_info = models.CharField(db_column='trolling info', max_length=200)  # Field renamed to remove unsuitable characters.
    starting_date = models.DateField(db_column='starting date')  # Field renamed to remove unsuitable characters.
    ending_date = models.DateField(db_column='ending date')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'trolling'

