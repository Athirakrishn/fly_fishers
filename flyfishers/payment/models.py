from django.db import models
from orders.models import Order
from fishermen.models import Fishermen
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # fishermen_id = models.IntegerField()
    fishermen=models.ForeignKey(Fishermen,on_delete=models.CASCADE)
    # order_id = models.IntegerField()
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    account_no = models.IntegerField(db_column='account no')  # Field renamed to remove unsuitable characters.
    amount = models.IntegerField()
    bank_name = models.CharField(db_column='bank name', max_length=45)  # Field renamed to remove unsuitable characters.
    branch_name = models.CharField(db_column='branch name', max_length=45)  # Field renamed to remove unsuitable characters.
    ifsc_code = models.CharField(db_column='ifsc code', max_length=45)  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'

