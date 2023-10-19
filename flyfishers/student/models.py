from django.db import models
from education_assistance.models import EducationalAssistance
from fishermen.models import Fishermen
# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(db_column='student name', max_length=45)  # Field renamed to remove unsuitable characters.
    student_class = models.IntegerField(db_column='student class')  # Field renamed to remove unsuitable characters.
    date_of_birth = models.DateField(db_column='date of birth')  # Field renamed to remove unsuitable characters.
    village = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    pin_code = models.IntegerField(db_column='pin code')  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=45)
    institution = models.CharField(max_length=45)
    mark = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # educational_assistance_id = models.CharField(max_length=45)
    educational_assistance=models.ForeignKey(EducationalAssistance,on_delete=models.CASCADE)
    # fishermen_id = models.IntegerField()
    fishermen = models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    fishermen_id_proof = models.CharField(max_length=400)
    relation_proof = models.CharField(db_column='relation proof',
                                      max_length=400)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'student'


