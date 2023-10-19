from django.db import models

# Create your models here.
class EducationalAssistance(models.Model):
    educational_assistance_id = models.AutoField(primary_key=True)
    scolarship_name = models.CharField(db_column='scolarship name', max_length=45)  # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'educational_assistance'


