from django.db import models

class Voucher(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    capacity  = models.IntegerField()

