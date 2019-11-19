from django.db import models

class CreditCard (models.Model):
    ccnumber = models.CharField(max_length=14, primary_key=True)
    name = models.CharField(max_length=50)
    expire = models.DateField()
    cvv = models.IntegerField()
