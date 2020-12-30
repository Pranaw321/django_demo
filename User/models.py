from django.db import models


class User(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phoneNo = models.IntegerField(blank=False)
    password = models.CharField(blank=False, max_length=20)
